from django.contrib import admin
from .models import Destination, Booking, Contact
from django.utils.html import format_html
from .models import Review

admin.site.register(Review)

# Destination admin
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)

# Booking admin
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'destination',
        'checkin',
        'checkout',
        'guests',
        'bus_type',
        'food_type',
        'budget',
        'created_at',
    )
    list_filter = ('destination', 'bus_type', 'food_type', 'budget', 'created_at')
    search_fields = ('user__username', 'destination')
    ordering = ('-created_at',)

# Contact admin
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    search_fields = ('name', 'email', 'phone')

