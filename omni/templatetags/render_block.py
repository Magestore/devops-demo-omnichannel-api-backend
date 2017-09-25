# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

register = template.Library()

def render_block():
    return 'render block'