# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from omni.models import user

# Create your views here.
def view(request):
    user.mylogout(request)
    return redirect('login')
