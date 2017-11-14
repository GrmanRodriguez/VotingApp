# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from main.models import Carousel
from django.template.response import TemplateResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    cardata = Carousel.objects.all()
    itercardata = iter(cardata)
    next(itercardata)
    if request.user.is_authenticated():
        username = request.user.username
        return TemplateResponse(request, 'main/hi.html', {"cardata": cardata, "itercardata": itercardata, "sizes": range(1, cardata.count()), "username": username})
    else:
        return TemplateResponse(request, 'main/hi.html', {"cardata": cardata, "itercardata": itercardata, "sizes": range(1, cardata.count())})
