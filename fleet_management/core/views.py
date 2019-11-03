from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from .models import *

@login_required
def list_vehicles(request):
    listx = Vehicle.objects.all()
    context ={"vehicles": listx}
    return render(request, "list_view.html", context)

@login_required
def reserve_vehicle(request, id):
    v = get_object_or_404(Vehicle, pk=id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.vehicle = v
            form.customer = User
            form.save()
            return redirect('core:list')
    else:
        form = ReservationForm()
        return redirect('core:list')

    return render(request, 'detail_view.html')

@login_required
def detail_view(request,id):
    v = get_object_or_404(Vehicle, pk=id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.customer = request.user
            form.vehicle = v
            form.save()
            return redirect('core:list')
    else:
        form = ReservationForm()
    return render(request, 'detail_view.html', {'form': form, 'object':v})

class VehicleDetailView(DetailView):
    template_name = 'detail_view.html'
    queryset = Vehicle.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Vehicle, id=id_)