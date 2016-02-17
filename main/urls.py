from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^register$', views.register, name='register'),
	url(r'^user_created$', views.user_created, name='user_created'),
	url(r'^$', views.register, name='register')
]