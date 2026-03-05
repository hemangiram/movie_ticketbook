from django.urls import path
from .views import book_ticket, my_bookings, cancel_booking



urlpatterns = [
    path('book/<int:pk>/', book_ticket, name='book_ticket'),
    path('my-bookings/', my_bookings, name='my_bookings'),
    path('cancel_booking/<int:booking_id>', cancel_booking, name='cancel_booking'),
    
]


