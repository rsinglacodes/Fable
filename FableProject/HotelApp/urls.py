from django.urls import path
from . import views

urlpatterns = [
    path('hotels/', views.Hotel_view, name='hotel_list'),
    path('hotels/<str:hotel_name>/', views.rooms_detail, name='room_detail'),
]