from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = (
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('index.urls')),
    url(r'^cards/', include('cards.urls', namespace='card')),
    url(r'^', include('social.apps.django_app.urls', namespace='social')),
    url(r'^', include('accounts.urls')),
)
