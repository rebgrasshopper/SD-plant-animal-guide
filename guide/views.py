from django.shortcuts import render, get_object_or_404
from .models import Plant

def plant_detail(request, pk):
    '''view for individual plant pages'''
    plant = get_object_or_404(Plant, pk=pk)
    return render(request, 'guide/plant_detail.html', { 'plant':plant })

def plant_list(request):
    '''view for main page'''
    native_plants = Plant.objects.filter(status='Native')
    non_native_plants = Plant.objects.filter(status='Non-native')
    invasive_plants = Plant.objects.filter(status='Invasive')
    return render(request, "guide/plant_list.html", {'native_plants':native_plants, 'non_native_plants':non_native_plants, 'invasive_plants':invasive_plants})
