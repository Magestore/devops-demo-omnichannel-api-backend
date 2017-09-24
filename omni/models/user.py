# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.db import models
from django.db.models import Model

class User(Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

## check authen user
def auth(request):
    u = request.POST['username']
    p = request.POST['password']
    return authenticate(username=u, password=p)

## Log in user
def mylogin(request):
    u = request.POST['username']
    p = request.POST['password']
    user = authenticate(request, username=u, password=p)
    if user is not None:
        login(request, user)
        return True
    else:
        return False

## Log out user
def mylogout(request):
    return logout(request)

