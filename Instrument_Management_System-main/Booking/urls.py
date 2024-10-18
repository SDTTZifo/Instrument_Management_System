
from django.contrib import admin
from django.urls import include, path

from Booking.views import booking_view, new_booking

urlpatterns = [
    path('booking/', booking_view, name='booking'),
    path('new-booking/', new_booking, name='new_booking'),
]
