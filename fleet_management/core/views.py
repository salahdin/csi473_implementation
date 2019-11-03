from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def list_vehicles(request):
    listx = Vehicle.objects.all()
    context ={"vehicles": listx}
    return render(request, "list_view.html", context)

@login_required
def reserve_vehicle(request, V_id):
    vehicle = get_object_or_404(Vehicle, pk=V_id)
    if request.method == 'POST':
        v = Reservation()


class VehicleDetailView(DetailView):
    template_name = 'detail_view.html'
    queryset = Vehicle.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Vehicle, id=id_)