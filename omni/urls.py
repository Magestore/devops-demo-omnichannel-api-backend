from django.conf.urls import url

from .views import index, site, template

app_name = 'omni'
urlpatterns = [
    url(r'^$', index.View.as_view(), name='index'),
    url(r'^sites/$', site.View.as_view(), name='sites'),
    url(r'^sites/(?P<pk>[0-9]+)/$', site.detail, name='site_edit'),
    url(r'^templates/$', template.View.as_view(), name='templates'),
    url(r'^templates/(?P<pk>[0-9]+)/$', template.detail, name='template_edit'),
]
