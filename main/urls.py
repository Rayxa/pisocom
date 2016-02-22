from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^$', views.main, name='home'),
]
