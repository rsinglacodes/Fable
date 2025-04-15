from django.shortcuts import render, redirect
from HotelApp.models import Hotel

def Hotel_view(request):
    category = request.GET.get('category', None)
    
    if category and category != 'all':
        hotel_list = Hotel.objects.filter(category=category)
    else:
        hotel_list = Hotel.objects.all()
        
    return render(request, "amazing.html", context={
        'hotel_list': hotel_list,
        'categories': Hotel.CATEGORIES,  
        'selected_category': category
    })