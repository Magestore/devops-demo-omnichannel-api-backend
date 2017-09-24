from django.conf.urls import url
from django.contrib import admin

import view_models

app_name = 'omni'
urlpatterns = [
    url(r'^$', view_models.Index.as_view(), name='index'),
    url(r'^sites/$', view_models.Sites.as_view()),
    url(r'^sites/(?P<pk>[0-9]+)/$', view_models.site.detail),
    url(r'^templates/$', view_models.Templates.as_view()),
    url(r'^templates/(?P<pk>[0-9]+)/$', view_models.templates.detail),
]
