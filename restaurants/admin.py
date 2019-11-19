from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')