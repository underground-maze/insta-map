from django.conf.urls import include, url
from accounts import views


urlpatterns = (
    url(r'^login', views.login_view, name='login'),
    url(r'^logout', views.logout_view, name='logout'),
    # django registration urls
    url(r'^email/', include('registration.backends.default.urls')),
)
