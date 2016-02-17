from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^nueva/$', 'main.views.newcasa'),
]