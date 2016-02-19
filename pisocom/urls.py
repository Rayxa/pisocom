from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register$', views.register, name='register'),
    url(r'^register/success$', views.user_created, name='user_created'),
	url(r'^captcha/', include('captcha.urls')),
]
