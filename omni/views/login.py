# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.
def view(request):

    def get(request):
        return repr(request)

    u = request.POST['username']
    p = request.POST['password']
    return render(request, 'login.html', {'user': {'u': u, 'p': p}})
