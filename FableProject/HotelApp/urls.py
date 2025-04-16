from django.urls import path
from . import views

urlpatterns = [
    path('hotels/', views.Hotel_view, name='hotel_list'),
    path('hotels/<slug:hotel_slug>/', views.rooms_detail, name='room_detail'),
]