from django.core.urlresolvers import reverse_lazy
from django.conf.urls import include, url

from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import forms


urlpatterns = (
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^s50admin/', include(admin.site.urls)),
    url(r'^', include('index.urls')),
    url(r'^cards/', include('cards.urls', namespace='card')),
    url(r'^', include('accounts.urls')),
    # registration urls
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^email/password/reset/$', auth_views.password_reset, {
        'post_reset_redirect': reverse_lazy('auth_password_reset_done'),
        'password_reset_form': forms.InstaPasswordResetForm,
    }, name='custom_password_reset'),
    url(r'^email/', include('registration.backends.default.urls')),
)
