
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'pages'

urlpatterns = [
	# main view
	path('', views.index, name='home'),
	path('add_product', views.add_product, name='add_product'),
	path('delete_product', views.delete_product, name='delete_product'),
	path('mark_product', views.mark_product, name='mark_product'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)