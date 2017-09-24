# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.basic import TemplateView
from django.urls import reverse

# Create your views here.
class Index(ListView):
    template_name = 'index.html'
    pass

class Sites(ListView):
    pass

class Templates(ListView):
    pass

