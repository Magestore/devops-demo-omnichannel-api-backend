# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from omni.models import objects
from omni.models.menu import Menu

# Create your views here.
class View(ListView):
    model = objects.Site
    template_name = 'index.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        global menu
        menu.setActive('index')
        return super(View, self).dispatch(*args, **kwargs)

    def getActiveMenu(self):
        return 'index'