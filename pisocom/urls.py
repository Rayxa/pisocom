"""poyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cuenta/login/$', 'pisocom.views.login'),
    url(r'^cuenta/auth/$', 'pisocom.views.auth_view'),
    url(r'^cuenta/logout/$', 'pisocom.views.logout'),
    url(r'^cuenta/loggedin/$', 'pisocom.views.loggedin'),
    url(r'^cuenta/invalid/$', 'pisocom.views.invalid_login'),
    url(r'^$', 'pisocom.views.main'),
]
