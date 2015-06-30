from django.conf.urls import patterns, url

urlpatterns = patterns(
    'index.views',
    url(r'^home$', 'index_view', name='index'),
    url(r'^update$', 'site_update_view', name='site_update'),
)
