from django.contrib import admin
from .models import *


class ReservationInline(admin.TabularInline):
    model = Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'rent_from', 'rent_to')
    search_fields = ['vehicle']


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_name','vehicle_type','photo')
    list_filter = ['vehicle_type']


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Vehicle, VehicleAdmin)
