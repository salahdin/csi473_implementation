from django.shortcuts import render
from .models import Vehicle

def list_vehicles(request):
    listx = Vehicle.objects.all()
    context ={"vehicles": listx}
    return render(request, "list_view.html", context)
