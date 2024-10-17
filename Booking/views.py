from django.shortcuts import render

def booking_view(request):
    return render(request, 'booking/booking.html')  

def new_booking(request):
    return render(request, 'booking/new_booking.html')  