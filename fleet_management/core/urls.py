from .import views
from django.urls import path,include

urlpatterns = [
    path("list/", views.list_vehicles, name="list"),
    path('detail/<int:id>/', views.VehicleDetailView.as_view(), name='vehicle_detail'),
]