# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from register.models import Singers
# Create your views here.


def index(request):
    singers = Singers.objects.all()
    return render(request, 'voting/vote.html', {'singers': singers})
