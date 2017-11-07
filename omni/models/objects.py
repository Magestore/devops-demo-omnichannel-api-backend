# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Model

# Create your models here.
class Extension(Model):
    model_id = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    repo_url = models.CharField(max_length=250)
    branch = models.CharField(max_length=100, default='master')

class Site(Model):
    site_id = models.IntegerField(default=0)
    url_path = models.CharField(max_length=300)
    admin_user = models.CharField(max_length=30)
    admin_password = models.CharField(max_length=60)
    db_name = models.CharField(max_length=100)
    db_user = models.CharField(max_length=100)
    db_password = models.CharField(max_length=60)
    framework = models.CharField(max_length=200)
    image = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    title = models.CharField(max_length=150)

class Template(Model):
    template_id = models.IntegerField(default=0)
    admin_user = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=60)
    db_name = models.CharField(max_length=100)
    db_user = models.CharField(max_length=100)
    db_password = models.CharField(max_length=60)
    framework = models.CharField(max_length=200)
    from_site = models.CharField(max_length=300)
    image = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)

class TemplateExtension(Model):
    temp_ext_id = models.IntegerField(default=0)
    extension_id = models.ForeignKey(Extension, on_delete=models.CASCADE)
    template_id = models.ForeignKey(Template, on_delete=models.CASCADE)

class SiteExtension(Model):
    site_ext_id = models.IntegerField(default=0)
    extension_id = models.ForeignKey(Extension, on_delete=models.CASCADE)
    template_id = models.ForeignKey(Site, on_delete=models.CASCADE)

class SiteOwner(Model):
    url_path = models.CharField(max_length=300)
    username = models.CharField(max_length=100)