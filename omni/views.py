# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.basic import TemplateView
from django.urls import reverse

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class Sites(ListView):
    template_name = 'sites.html'

class Templates(ListView):
    template_name = 'templates.html'

