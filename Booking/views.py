from django.shortcuts import redirect, render
from Booking.models import Booking

def booking_view(request):
    return render(request, 'booking/booking.html')  

def new_booking(request):
    if request.method == 'POST':
        equipment_category = request.POST['equipment_category']
        equipment = request.POST['equipment']
        location = request.POST['location']
        maintenance_date = request.POST.get('maintenance_date')
        booking_start_date = request.POST['booking_start_date']
        booking_end_date = request.POST['booking_end_date']
        status = request.POST['status']
        booked_by = request.POST['booked_by']
        reason = request.POST.get('reason', '')

        # Create a new booking instance
        booking = Booking(
            equipment_category=equipment_category,
            equipment=equipment,
            location=location,
            maintenance_date=maintenance_date,
            booking_start_date=booking_start_date,
            booking_end_date=booking_end_date,
            status=status,
            booked_by=booked_by,
            reason=reason
        )
        
        # Save the booking to the database
        booking.save()
        
        # Redirect to bookings page after saving
        return redirect('booking')

    return render(request, 'booking/new_booking.html')