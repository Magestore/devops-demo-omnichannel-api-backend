# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from omni.models import objects
from omni.models import user

class Site(objects.Site):

    ## return user.User object
    def getOwner(self):
        owner_name = self.getOwnerName()
        return user.User.objects.get(username=owner_name)

    def getOwnerName(self):
        return self.getSiteOwner().username

    def getSiteOwner(self):
        return objects.SiteOwner.objects.get(url_path=self.url_path)
