# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from omni.models import objects

# Register your models here.

admin.site.register(objects.Site)
admin.site.register(objects.Template)
admin.site.register(objects.Extension)
