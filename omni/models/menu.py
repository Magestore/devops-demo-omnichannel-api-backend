# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Menu():

    active = 'index'
    item = []

    def __init__(self):
        self.item.append(self.active)

    def setActive(self, active=''):
        self.active = active
        return self

    def getActive(self):
        return self.active
