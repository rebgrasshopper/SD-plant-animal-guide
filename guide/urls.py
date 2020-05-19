from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static



urlpatterns = [
    path('', views.plant_list, name='plant_list'),
    path('plant/<int:pk>/', views.plant_detail, name='plant_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)