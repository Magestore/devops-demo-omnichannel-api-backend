# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.basic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
