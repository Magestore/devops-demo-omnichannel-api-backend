# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.urls import reverse

class View(ListView):
    template_name = 'templates.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(View, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return {'ok':'ok'}

# Create your views here.
def detail(request, template_id):
    pass
