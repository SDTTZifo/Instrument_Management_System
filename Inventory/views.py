from django.shortcuts import redirect, render
from .models import Instrument, Category
from django.db.models import Q

def HomePage(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def instruments_view(request):
    instruments = Instrument.objects.all()  # Retrieve all instrument records
    return render(request, 'instruments/instruments.html', {'instruments': instruments})

def add_instrument_view(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        instrument_name = request.POST.get('instrument_name')
        category = request.POST.get('category')
        model_number = request.POST.get('model_number')
        manufacturer = request.POST.get('manufacturer')
        purchased_On = request.POST.get('purchased_On')
        owned_by = request.POST.get('owned_by')
        location = request.POST.get('location')
        status = request.POST.get('status')
        maintenance_date = request.POST.get('maintenance_date')

        # Create a new instrument object and save it to the database
        new_instrument = Instrument(
            instrument_name=instrument_name,
            category= category,
            model_number = model_number,
            manufacturer = manufacturer,
            purchased_On = purchased_On,
            owned_by =  owned_by,
            location =  location,
            status = status,
            maintenance_date =  maintenance_date    
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

def search_instrument_view(request):      

    query = request.GET.get("query")
    instruments = Instrument.objects.all()
    if query:
        instruments = instruments.filter(
                                            Q(instrument_name__icontains=query)|
                                            Q(category__icontains=query)|
                                            Q(model_number__icontains=query)|
                                            Q(status__icontains=query))
        
                                        

    return render(request, 'instruments/instruments.html', {'instruments': instruments, 'query' : query})