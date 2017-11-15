# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Votes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    participant_vote_id = models.IntegerField()
