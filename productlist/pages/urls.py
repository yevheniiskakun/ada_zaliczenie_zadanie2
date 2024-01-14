
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'pages'

urlpatterns = [
	# main view
	path('', views.index, name='home'),
	path('add_product/<str>', views.add_product, name='add_product'),
	path('delete_product/<int:id>', views.delete_product, name='delete_product'),
	path('mark_product/<int>', views.mark_product, name='mark_product'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)