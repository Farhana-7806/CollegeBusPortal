from django.shortcuts import render

def bus_map(request):
    return render(request, 'map.html')
