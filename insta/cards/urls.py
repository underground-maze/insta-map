from django.conf.urls import patterns, url

urlpatterns = patterns(
    'cards.views',
    url(r'^add$', 'add_card_view', name='add'),
)
