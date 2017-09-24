from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'omni'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^sites/$', views.Sites.as_view()),
    url(r'^sites/(?P<pk>[0-9]+)/$', views.site.detail),
    url(r'^templates/$', views.Templates.as_view()),
    url(r'^templates/(?P<pk>[0-9]+)/$', views.templates.detail),
]
