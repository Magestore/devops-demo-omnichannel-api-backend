# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from omni import models

# Register your models here.

admin.site.register(models.Site)
admin.site.register(models.Template)
admin.site.register(models.Extension)
