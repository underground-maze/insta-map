from django.conf.urls import url
from index import views

urlpatterns = (
    url(r'^home$', views.IndexView.as_view(), name='index'),
    url(r'^update$', views.SiteUpdate.as_view(), name='site_update'),
    url(r'^anonymous$', views.IndexMenuView.as_view(), name='anonymous_view'),
)
