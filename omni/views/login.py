# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import View

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {'user': {'u': '', 'p': ''}})

    def post(self, request, *args, **kwargs):
        u = request.GET['username']
        p = request.GET['password']
        return render(request, 'login_post.html', {'user': {'u': u, 'p': p}})
