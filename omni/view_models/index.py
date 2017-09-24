# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import basic

# Create your views here.
class IndexView(basic.TemplateView):
    template_name = 'index.html'
