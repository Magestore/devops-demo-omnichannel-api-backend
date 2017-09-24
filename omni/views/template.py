# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.urls import reverse

class View(ListView):
    template_name = 'templates.html'


# Create your views here.
def detail(request, id):
    pass
