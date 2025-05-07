from django.contrib import admin
from HotelApp.models import Hotel

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name', 'price', 'location', 'category', 'image1_url', 'image2_url', 'image3_url', 'image4_url', 'image5_url']
    list_filter = ['category', 'location']
    search_fields = ['hotel_name', 'location', 'category']

admin.site.register(Hotel, HotelAdmin)
