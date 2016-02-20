from django.conf.urls import include, url
from . import views
import main.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^crear_direccion/', main.views.crear_direccion),
    url(r'^crear_casa/', main.views.crear_casa),
	url(r'^casa_creada/', main.views.casa_creada),
	
]