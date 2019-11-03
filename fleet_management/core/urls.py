from .import views
from django.urls import path

app_name = 'core'
urlpatterns = [
    path("list/", views.list_vehicles, name="list"),
    path("detail/<int:id>/", views.detail_view, name='vehicle_detail'),
    path("reserve/<int:id>/", views.reserve_vehicle , name='res'),
]