from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/login/$', views.login),
    url(r'^user/auth/$', views.auth_view),
    url(r'^user/logout/$', views.logout),
    url(r'^user/loggedin/$', views.loggedin),
    url(r'^user/invalid/$', views.invalid_login),
    url(r'^user/register/$', views.register),
    url(r'^user/register/success/$', views.user_created),

    url(r'^user/password/reset/$', auth_views.password_reset,
    {'template_name' : 'user/password/password_reset.html', 'post_reset_redirect' : 'done/'}),

    url(r'^user/password/reset/done/$', auth_views.password_reset_done,
    {'template_name' : 'user/password/password_reset_done.html',}),

    url(r'^user/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    auth_views.password_reset_confirm,
    {'template_name' : 'user/password/password_reset_confirm.html'},
    name='password_reset_confirm'),

    url(r'^user/password/reset/complete/$',
    auth_views.password_reset_complete,
    {'template_name' : 'user/password/password_reset_complete.html'},
    name='password_reset_complete'),

	url(r'^captcha/', include('captcha.urls')),
    url(r'^$', views.main),
]
