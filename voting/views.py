# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from register.models import Singers

# Create your views here.


def index(request):
    # singers = Singers.objects.filter(Q(id=backend.singer1) | Q(id=backend.singer2))
    singers = Singers.objects.all()
    if request.user.is_authenticated():
        username = request.user.username
        return render(request, 'voting/vote.html', {'singers': singers, 'amount': Singers.objects.all().count(), 'username': username})
    else:
        return render(request, 'voting/vote.html', {'singers': singers, 'amount': Singers.objects.all().count()})
