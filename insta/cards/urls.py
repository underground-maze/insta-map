from django.conf.urls import url
from cards import views

urlpatterns = (
    url(r'^add$', views.AddCardView.as_view(), name='add'),
)
