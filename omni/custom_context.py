# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import RequestContext
from omni.models.menu import Menu

def menu_context(request):

    return {'menu': menu}
