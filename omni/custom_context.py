# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import RequestContext
from omni.models.menu import Menu

## Global menu variable
menu = Menu()

def menu_context(request):
    global menu
    return {'menu': menu}
