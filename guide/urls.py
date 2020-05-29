from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static



urlpatterns = [
    path('', views.plant_list, name='plant_list'),
    path('plant/<slug:slug>/', views.plant_detail, name='plant_detail'),
    path('about/', views.about, name='about')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)