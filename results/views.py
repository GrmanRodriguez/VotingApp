# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pygal
from pygal.style import Style
from django.shortcuts import render
from django.db.models import Q
from register.models import Singers
from voting.models import Votes, VoteAdmin as VA

# Create your views here.


def index(request):
  custom_style1 = Style(font_family='quiroh, sans-serif',
                        background='transparent',
                        foreground='#5A4B66',
                        tooltip_font_size='50',
                        plot_background='transparent',
                        transition='400ms ease-in')
  sessions = VA.objects.all()
  cnt = 0
  titles = []
  for x in sessions:
    pie_chart = pygal.Pie(inner_radius=.75, style=custom_style1)
    pie_chart.force_uri_protocol = 'https'
    votes_first = Votes.objects.filter(Q(date__lte=x.end_date), Q(date__gte=x.start_date), Q(participant_vote_id=x.participant_1)).count()
    votes_secnd = Votes.objects.filter(Q(date__lte=x.end_date), Q(date__gte=x.start_date), Q(participant_vote_id=x.participant_2)).count()
    if votes_first > votes_secnd:
      pie_chart.add(Singers.objects.get(id=x.participant_1).name,
                    Votes.objects.filter(Q(date__lte=x.end_date), Q(date__gte=x.start_date), Q(participant_vote_id=x.participant_1)).count())
      pie_chart.add(Singers.objects.get(id=x.participant_2).name,
                    Votes.objects.filter(Q(date__lte=x.end_date), Q(date__gte=x.start_date), Q(participant_vote_id=x.participant_2)).count())
      newtitle = "Round " + str(cnt + 1) + ": Looks Like " + Singers.objects.get(id=x.participant_1).name + " Has Been Eliminated!"
      titles.append(newtitle)
    elif votes_first < votes_secnd:
      pie_chart.add(Singers.objects.get(id=x.participant_1).name,
                    Votes.objects.filter(Q(date__lte=x.end_date), Q(date__gte=x.start_date), Q(participant_vote_id=x.participant_1)).count())
      pie_chart.add(Singers.objects.get(id=x.participant_2).name,
                    Votes.objects.filter(Q(date__lte=x.end_date), Q(date__gte=x.start_date), Q(participant_vote_id=x.participant_2)).count())
      newtitle = "Round " + str(cnt + 1) + ": Looks Like " + Singers.objects.get(id=x.participant_2).name + " Has Been Eliminated!"
      titles.append(newtitle)
    else:
      pie_chart.add(Singers.objects.get(id=x.participant_1).name,
                    Votes.objects.filter(Q(date__lte=x.end_date), Q(date__gte=x.start_date), Q(participant_vote_id=x.participant_1)).count())
      pie_chart.add(Singers.objects.get(id=x.participant_2).name,
                    Votes.objects.filter(Q(date__lte=x.end_date), Q(date__gte=x.start_date), Q(participant_vote_id=x.participant_2)).count())
      newtitle = "Round " + str(cnt + 1) + ": " + "Both Participants Were Eliminated As There Was A Draw!"
      titles.append(newtitle)
    chart_title = 'results/static/results/pie' + str(cnt + 1) + '.svg'
    pie_chart.render_to_file(chart_title)
    cnt += 1
  if request.user.is_authenticated():
    return render(request, 'results/results.html', {'username': request.user.username, 'titles': titles})
  else:
    return render(request, 'results/results.html', {'titles': titles, 'cnt': 0})
