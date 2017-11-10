# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from omni.models.menu import Menu

class OmniConfig(AppConfig):
    name = 'omni'

## Global menu variable
menu = Menu()
