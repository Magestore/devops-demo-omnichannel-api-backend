# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.urls import reverse

class SitesView(generic.ListView):
    template_name = 'sites.html'

# Create your views here.
def detail(request, id):
    pass


