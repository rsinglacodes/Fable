from django.urls import path
from . import views

urlpatterns = [
    path('', views.Hotel_view, name='amazing'), 
    path('hotels/', views.Hotel_view, name='hotel_list'),
    path('hotels/<slug:hotel_slug>/', views.rooms_detail, name='room_detail'),
    path('confirm/', views.confirm_booking, name='confirm_booking'),
    path('book-room/', views.book_room, name='book_room'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]