from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('delete/<str:pk>/', views.delete_image, name = 'delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)