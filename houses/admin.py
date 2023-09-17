from django.contrib import admin
from .models import House
# Register your models here.

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    
    list_display = [
        "name",
        "price_per_night",
        "address",
        "isBooked"
    ]

    list_filter = ["price_per_night", "isBooked"]

    search_fields = ["address"]

    list_display_links = ["name", "address"]

