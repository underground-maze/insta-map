from django.core.urlresolvers import reverse_lazy
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from accounts import views
from accounts import forms


urlpatterns = (
    url(r'^login', views.login_view, name='login'),
    url(r'^logout', views.logout_view, name='logout'),
    # django registration urls
    url(r'^email/password/reset/$', auth_views.password_reset, {
        'post_reset_redirect': reverse_lazy('auth_password_reset_done'),
        'password_reset_form': forms.InstaPasswordResetForm,
    }, name='custom_password_reset'),

    url(r'^email/', include('registration.backends.default.urls')),
)
