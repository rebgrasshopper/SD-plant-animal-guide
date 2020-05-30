from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.plant_list, name='plant_list'),
    path('plant/<slug:slug>/', views.plant_detail, name='plant_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search_results, name='search_results'),
    path('native_plants/', views.native_plants_list, name='native_plants_list'),
    path('non_native_plants/', views.non_native_plants_list, name='non_native_plants_list'),
    path('invasive_plants/', views.invasive_plants_list, name='invasive_plants_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)