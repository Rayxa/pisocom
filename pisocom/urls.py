from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/auth/$', views.auth_view, name='auth'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'^accounts/invalid/$', views.invalid_login, name='invalid'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/register/success/$', views.user_created, name='register_success'),

    url(r'^accounts/password/reset/$',
    auth_views.password_reset,
    {'template_name' : 'accounts/password/password_reset.html', 'post_reset_redirect' : 'password_reset_done'},
    name='password_reset'),

    url(r'^accounts/password/reset/done/$',
    auth_views.password_reset_done,
    {'template_name' : 'accounts/password/password_reset_done.html'},
    name='password_reset_done'),

    url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    auth_views.password_reset_confirm,
    {'template_name' : 'accounts/password/password_reset_confirm.html'},
    name='password_reset_confirm'),

    url(r'^accounts/password/reset/complete/$',
    auth_views.password_reset_complete,
    {'template_name' : 'accounts/password/password_reset_complete.html'},
    name='password_reset_complete'),

	url(r'^captcha/', include('captcha.urls')),
    url(r'', include('main.urls')),
]
