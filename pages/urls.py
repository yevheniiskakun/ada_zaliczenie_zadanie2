from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'pages'

urlpatterns = [
	# main view
	path('', views.index, name='home'),
	path('delete_image', views.delete_image, name='delete_image'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)