
from django.contrib import admin
from django.urls import include, path

from Booking.views import booking_view

urlpatterns = [
    path('booking/', booking_view, name='booking'),  # Add booking view
]
