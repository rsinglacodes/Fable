from django.shortcuts import render, redirect, get_object_or_404
from HotelApp.models import Hotel, Booking
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import logging

# Configure logging
logger = logging.getLogger(__name__)

def Hotel_view(request):
    category = request.GET.get('category', None)
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)
    guests = request.GET.get('guests', None)
    
    hotel_list = Hotel.objects.all()
    
    if category and category != 'all':
        hotel_list = hotel_list.filter(category=category)
    
    if min_price:
        hotel_list = hotel_list.filter(price__gte=float(min_price))
    
    if max_price:
        hotel_list = hotel_list.filter(price__lte=float(max_price))
    
    if guests:
        hotel_list = hotel_list.filter(guests__gte=int(guests))
        
    return render(request, "amazing.html", context={
        'hotel_list': hotel_list,
        'categories': Hotel.CATEGORIES,
        'selected_category': category,
        'min_price': min_price,
        'max_price': max_price,
        'guests_filter': guests
    })

def rooms_detail(request, hotel_slug):
    room = get_object_or_404(Hotel, slug=hotel_slug)
    
    context = {
        'room': room,
        'rating': 4.8, 
        'review_count': 42,  
    }
    
    return render(request, 'rooms.html', context)

def dashboard_view(request):
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)
    guests = request.GET.get('guests', None)
    
    hotel_list = Hotel.objects.all()
    
    if min_price:
        hotel_list = hotel_list.filter(price__gte=float(min_price))
    if max_price:
        hotel_list = hotel_list.filter(price__lte=float(max_price))
    if guests:
        hotel_list = hotel_list.filter(guests__gte=int(guests))
    
    return render(request, "dashboard.html", context={
        'hotel_list': hotel_list,
        'min_price': min_price,
        'max_price': max_price,
        'guests_filter': guests
    })

def confirm_booking(request):
    room_id = request.GET.get('room_id')
    check_in_str = request.GET.get('check_in')
    check_out_str = request.GET.get('check_out')
    guests = request.GET.get('guests', 1)

    room = get_object_or_404(Hotel, hotel_name=room_id)

    try:
        check_in = datetime.strptime(check_in_str, '%Y-%m-%d')
        check_out = datetime.strptime(check_out_str, '%Y-%m-%d')
        nights = (check_out - check_in).days
        total_price = room.price * nights
    except (ValueError, TypeError):
        check_in = datetime.now()
        check_out = datetime.now()
        nights = 1
        total_price = room.price

    user = request.user if request.user.is_authenticated else None

    context = {
        'room': room,
        'check_in': check_in_str,
        'check_out': check_out_str,
        'guests': guests,
        'nights': nights,
        'total_price': total_price,
        'user': user
    }

    return render(request, 'confirm.html', context)

@login_required
def book_room(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        check_in_str = request.POST.get('check_in')
        check_out_str = request.POST.get('check_out')
        guests = request.POST.get('guests', 1)
        total_price = float(request.POST.get('total_price', 0))

        hotel = get_object_or_404(Hotel, hotel_name=room_id)

        try:
            booking = Booking(
                hotel_name=hotel,
                user=request.user,
                check_in=datetime.strptime(check_in_str, '%Y-%m-%d'),
                check_out=datetime.strptime(check_out_str, '%Y-%m-%d'),
                guests=int(guests),
                total_price=total_price
            )
            
            booking.save()
            logger.debug(f"Booking created with ID: {booking.id}")
            messages.success(request, 'Room booked successfully!')
            return JsonResponse({'success': True, 'booking_id': str(booking.id)})
        except Exception as e:
            logger.error(f"Error booking room: {str(e)}")
            messages.error(request, f'Error booking room: {str(e)}')
            return JsonResponse({'success': False, 'error': str(e)})
    
    return redirect('amazing')