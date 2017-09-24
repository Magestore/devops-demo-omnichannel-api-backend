# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
#from django.views.generic import ListView
#from django.views.generic.basic import TemplateView

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'


class SitesView(generic.ListView):
    template_name = 'sites.html'

# Create your views here.
def detail(request, id):
    pass


