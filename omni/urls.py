from django.conf.urls import url

from omni import views

app_name = 'omni'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^sites/$', views.Sites.as_view(), name='sites'),
    url(r'^sites/(?P<pk>[0-9]+)/$', view_models.site.detail, name='site_edit'),
    url(r'^templates/$', views.Templates.as_view(), name='templates'),
    url(r'^templates/(?P<pk>[0-9]+)/$', view_models.templates.detail, name='template_edit'),
]
