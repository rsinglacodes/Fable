from django.shortcuts import render, get_object_or_404
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



def rooms_detail(request, hotel_name):
    # Get the hotel object from your database using the hotel_name
    room = get_object_or_404(Hotel, hotel_name=hotel_name)
    
    context = {
        'room': room,
        'rating': 4.8,  # You might want to make this dynamic based on actual reviews
        'review_count': 42,  # Same here
    }
    
    return render(request, 'rooms.html', context)