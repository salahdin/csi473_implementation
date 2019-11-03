from .import views
from django.urls import path,include

urlpatterns = [
    path("list/",views.list_vehicles,name="list"),
]