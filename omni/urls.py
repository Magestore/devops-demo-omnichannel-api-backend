from django.conf.urls import url

from .views import *

app_name = 'omni'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^sites/$', SitesView.as_view(), name='sites'),
    url(r'^sites/(?P<pk>[0-9]+)/$', sites.detail, name='site_edit'),
    url(r'^templates/$', TemplatesView.as_view(), name='templates'),
    url(r'^templates/(?P<pk>[0-9]+)/$', templates.detail, name='template_edit'),
]
