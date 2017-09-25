# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import View

# Create your views here.
def view(request):
    u = 'default' # request.GET['username']
    p = 'default' # request.GET['password']
    return render(request, 'login.html', {'user': {'u': u, 'p': p}})

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('This is GET request')

    def post(self, request, *args, **kwargs):
        return HttpResponse('This is POST request')
