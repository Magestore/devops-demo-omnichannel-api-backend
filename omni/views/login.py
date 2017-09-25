# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import View
from omni.models import user

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {'user': {'u': '', 'p': ''}})

    def post(self, request, *args, **kwargs):
        u = request.POST['username']
        p = request.POST['password']

        next = 'next=' + request.GET.get('next', '')

        return redirect(reverse('omni:templates', args=[next]))

        if user.mylogin(request):

            return redirect(reverse('login', args=[next]))
        else:
            return redirect(reverse('login', args=['next='+request.path]))
        return render(request, 'login_post.html', {'user': {'u': u, 'p': p}})
