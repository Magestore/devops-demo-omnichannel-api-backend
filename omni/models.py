# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Model

# Create your models here.
class Site(Model):
    id = models.IntegerField(default=0)
    url_path = models.CharField(max_length=30)
    admin_user = models.CharField(max_length=30)
    admin_password = models.CharField(max_length=60)
    db_name = models.CharField(max_length=100)
    db_user = models.CharField(max_length=100)
    db_password = models.CharField(max_length=60)
    extensions = models.ForeignKey(Extension, on_delete=models.CASCADE)
    framework = models.CharField(max_length=200)
    image = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    title = models.CharField(max_length=50)


class Template(Model):
    id = models.IntegerField(default=0)
    admin_user = models.CharField(max_length=30)
    admin_password = models.CharField(max_length=60)
    db_name = models.CharField(max_length=100)
    db_user = models.CharField(max_length=100)
    db_password = models.CharField(max_length=60)
    extensions = models.ForeignKey(Extension, on_delete=models.CASCADE)
    framework = models.CharField(max_length=200)
    from_site = models.CharField(max_length=200)
    image = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)


class Extension(Model):
    id = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    repo_url = models.CharField(max_length=150)
    branch = models.CharField(max_length=30, default='master')
