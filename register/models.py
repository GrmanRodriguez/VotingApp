# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Singers(models.Model):
    name = models.CharField(max_length=45)
    bio = models.CharField(max_length=500)
    img = models.ImageField(upload_to='singerpics/')
