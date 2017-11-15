# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template.response import TemplateResponse

from django.shortcuts import render, redirect

from register.models import Singers

from models import Votes
# Create your views here.


def index(request):
    singers = Singers.objects.all()
    if request.user.is_authenticated():
        if Votes.objects.filter(user=request.user).exists():
            votedfor = Singers.objects.get(id=Votes.objects.get(user=request.user).participant_vote_id).name
            return render(request, 'voting/vote.html', {'singers': Singers.objects.all(), 'voted': True, 'votedfor': votedfor, 'username': request.user.username})
        else:
            username = request.user.username
            return render(request, 'voting/vote.html', {'singers': singers, 'signed': True, 'username': username})
    else:
        return render(request, 'voting/vote.html', {'singers': singers})


def voteregister(request, pk):
    pk = int(pk)
    amountsingers = int(Singers.objects.latest('pk').pk)
    if pk > amountsingers:
        raise TemplateResponse('{% debug %}')
    else:
        if request.user.is_authenticated():
            if Votes.objects.filter(user=request.user).exists():
                return redirect('/vote/')
            else:
                vote = Votes(user=request.user, participant_vote_id=pk)
                vote.save()
                return redirect('/vote/')
