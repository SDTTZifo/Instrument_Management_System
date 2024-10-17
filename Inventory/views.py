from django.shortcuts import redirect, render
from .models import Instrument, Category
from django.shortcuts import redirect, render, get_object_or_404

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

def edit_category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)  # Fetch the category or return 404 if not found

    if request.method == 'POST':
        category.category_name = request.POST.get('category_name')
        category.category_description = request.POST.get('category_description')
        category.save()  # Save the updated category to the database

        return redirect('categories')  # Redirect to categories view after saving

    return render(request, 'categories/edit_category.html', {'category': category})

def delete_category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()  # Delete the category
        return redirect('categories')  # Redirect to categories view after deletion

    return render(request, 'categories/delete_category.html', {'category': category})