from django.shortcuts import render, get_object_or_404
from .models import Plant

def plant_detail(request, pk):
    '''view for individual plant pages'''
    plant = get_object_or_404(Plant, pk=pk)
    return render(request, 'guide/plant_detail.html', { 'plant':plant })
