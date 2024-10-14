from django.shortcuts import redirect, render
from .models import Instrument

def HomePage(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def instruments_view(request):
    instruments = Instrument.objects.all()  # Retrieve all instrument records
    return render(request, 'instruments/instruments.html', {'instruments': instruments})

def add_instrument_view(request):
    if request.method == 'POST':
        instrument_name = request.POST.get('instrument_name')
        instrument_description = request.POST.get('instrument_description')
        owned_by = request.POST.get('owned_by')

        # Create a new instrument object and save it to the database
        new_instrument = Instrument(
            instrument_name=instrument_name,
            instrument_description=instrument_description,
            owned_by=owned_by
        )
        new_instrument.save()  # Save to database

        return redirect('instruments')  # Redirect to instruments view after saving

    return render(request, 'instruments/add_instrument.html')