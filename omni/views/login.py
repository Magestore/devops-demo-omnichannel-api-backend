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
        if user.mylogin(request):
            next = request.GET.get('next', '')
            if next:
                return redirect(next)
            else:
                return redirect('omni:index')
        else:
            request.session['username'] = redirect.POST.get('username', '')
            request.session['password'] = redirect.POST.get('password', '')
            return redirect(reverse('omni:login'))

