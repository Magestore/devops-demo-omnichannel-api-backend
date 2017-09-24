# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic

# Create your views here.
class IndexView(generic.basic.TemplateView):
    template_name = 'index.html'
