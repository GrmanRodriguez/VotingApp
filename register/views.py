# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from register.forms import *
from django.contrib.auth import login as log_in, authenticate
from django.urls import reverse_lazy

# Create your views here.


def signup(request):
    if request.user.is_authenticated():
        username = request.user.username
        if request.method == 'GET':
            voter = Voter()
            singer = Singer()
            return render(request, 'register/signup.html', {'voter': voter, 'singer': singer, 'username': username})
        if request.method == 'POST':
            if 'email' in request.POST:
                voter = Voter(request.POST)
                if voter.is_valid():
                    voter.save()
                    user = authenticate(request, username=voter.username, password=voter.password1)
                    log_in(request, user)
                    return render(request, 'register/signup.html', {'voter': Voter(), 'singer': Singer(), 'success': True, 'username': username})
                else:
                    return render(request, 'register/signup.html', {'voter': Voter(), 'singer': Singer(), 'failure': True, 'username': username})
            elif 'bio' in request.POST:
                singer = Singer(request.POST, request.FILES)
                if singer.is_valid():
                    singer.save()
                    return render(request, 'register/signup.html', {'voter': Voter(), 'singer': Singer(), 'success': True, 'username': username})
                else:
                    return render(request, 'register/signup.html', {'voter': Voter(), 'singer': Singer(), 'failure': True, 'username': username})
            else:
                return render(request, 'register/signup.html', {'voter': Voter(), 'singer': Singer(), 'username': username})
    else:
        if request.method == 'GET':
            voter = Voter()
            singer = Singer()
            return render(request, 'register/signup.html', {'voter': voter, 'singer': singer})
        if request.method == 'POST':
            if 'email' in request.POST:
                voter = Voter(request.POST)
                if voter.is_valid():
                    voter.save()
                    return render(request, 'register/signup.html', {'voter': Voter(), 'singer': Singer(), 'success': True})
                else:
                    return render(request, 'register/signup.html', {'voter': Voter(), 'singer': Singer(), 'failure': True})
            elif 'bio' in request.POST:
                singer = Singer(request.POST, request.FILES)
                if singer.is_valid():
                    singer.save()
                    return render(request, 'register/signup.html', {'voter': Voter(), 'singer': Singer(), 'success': True})
                else:
                    return render(request, 'register/signup.html', {'voter': Voter(), 'singer': Singer(), 'failure': True})
            else:
                return render(request, 'register/signup.html', {'voter': Voter(), 'singer': Singer()})
