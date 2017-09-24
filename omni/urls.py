from django.conf.urls import url

from . import view_models

app_name = 'omni'
urlpatterns = [
    url(r'^$', view_models.index.IndexView.as_view(), name='index'),
    url(r'^sites/$', view_models.sites.SitesView.as_view(), name='sites'),
    url(r'^sites/(?P<pk>[0-9]+)/$', view_models.sites.detail, name='site_edit'),
    url(r'^templates/$', view_models.templates.Templates.as_view(), name='templates'),
    url(r'^templates/(?P<pk>[0-9]+)/$', view_models.templates.detail, name='template_edit'),
]
