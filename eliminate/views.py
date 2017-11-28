# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, redirect
from register.models import Singers
import yagmail
from django.db.models import Q
from voting.models import VoteAdmin as VA, Votes
# Create your views here.


def index(request):
    last_sd = VA.objects.latest('start_date').start_date
    last_ed = VA.objects.latest('start_date').end_date
    singer1 = Singers.objects.get(id=VA.objects.latest('start_date').participant_1)
    singer2 = Singers.objects.get(id=VA.objects.latest('start_date').participant_2)
    if timezone.now() > last_sd and timezone.now() < last_ed:
        if request.user.is_authenticated():
            if Votes.objects.filter(Q(user_id=request.user.id), Q(date__gte=last_sd), Q(date__lte=last_ed)).exists():
                votedfor = Singers.objects.get(id=Votes.objects.get(Q(user_id=request.user.id), Q(date__gte=last_sd), Q(date__lte=last_ed)).participant_vote_id)
                variables = {'singer1': singer1,
                             'singer2': singer2,
                             'username': request.user.username,
                             'active': True,
                             'voted': True,
                             'votedfor': votedfor}
            else:
                variables = {'singer1': singer1,
                             'singer2': singer2,
                             'username': request.user.username,
                             'active': True,
                             'logged': True}
        else:
            variables = {'singer1': singer1,
                         'singer2': singer2,
                         'active': True,
                         }
    else:
        if request.user.is_authenticated():
            variables = {'username': request.user.username}
        else:
            variables = {}
    return render(request, 'eliminate/eliminate.html', variables)


def voteattempt(request, pk):
    if request.method == 'POST':
        vote = Votes(user=request.user, participant_vote_id=pk, date=timezone.now())
        vote.save()
        yag = yagmail.SMTP('youremailhere@email.com','thepassword')
        cont = "Thanks for using VotingApp! You have voted for " + Singers.objects.get(id=pk).name
        yag.send(request.user.email, subject="You Voted in VotingApp!", contents = cont)
        return redirect('/eliminate/')
    else:
        return redirect('/eliminate/')
