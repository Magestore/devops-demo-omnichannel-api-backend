from django.conf.urls import url

from .view_models import index, sites, templates

app_name = 'omni'
urlpatterns = [
    url(r'^$', index.IndexView.as_view(), name='index'),
    url(r'^sites/$', sites.SitesView.as_view(), name='sites'),
    url(r'^sites/(?P<pk>[0-9]+)/$', sites.detail, name='site_edit'),
    url(r'^templates/$', templates.Templates.as_view(), name='templates'),
    url(r'^templates/(?P<pk>[0-9]+)/$', templates.detail, name='template_edit'),
]
