from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Instrument, Category

def HomePage(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def instruments_view(request):
    messages.success(request, "Welcome to the instrument page!")
    instruments = Instrument.objects.all()  # Retrieve all instrument records
    return render(request, 'instruments/instruments.html', {'instruments': instruments,'modal_title': 'modal_title'})

def add_instrument_view(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        instrument_name = request.POST.get('instrument_name')
        instrument_description = request.POST.get('instrument_description')
        owned_by = request.POST.get('owned_by')
        instrument_category_id = request.POST.get('instrument_category')  # Ensure this is the ID

        # Create a new instrument object and save it to the database
        new_instrument = Instrument(
            instrument_name=instrument_name,
            owned_by=owned_by,
            instrument_category_id=instrument_category_id  # Use the ID here
        )
        new_instrument.save()  # Save to database

        return redirect('instruments')  # Redirect to instruments view after saving

    return render(request, 'instruments/add_instrument.html', {'categories': categories})


def category_view(request):
    categories = Category.objects.all()  # Retrieve all instrument records
    return render(request, 'categories/categories.html', {'categories': categories})


def add_category_view(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        category_description = request.POST.get('category_description')       

        # Create a new category object and save it to the database
        new_category = Category(
            category_name=category_name,
            category_description=category_description
        )
        new_category.save()  # Save to database

        return redirect('categories')  # Redirect to categories view after saving

    return render(request, 'categories/add_category.html')