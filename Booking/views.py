from django.shortcuts import render

def booking_view(request):
    return render(request, 'booking/booking.html')  # Create booking.html template