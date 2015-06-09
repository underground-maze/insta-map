from django.conf.urls import patterns, url

urlpatterns = patterns(
    'index.views',
    url(r'^$', 'index_view', name='index'),
)
