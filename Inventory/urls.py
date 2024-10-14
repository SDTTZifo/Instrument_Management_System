from django.urls import include, path
from .views import *

urlpatterns = [
    path('', HomePage, name='index'),
    path('home/', HomePage),
    path('instruments/', instruments_view, name='instruments'),  # Add instruments view
    path('add-instrument/', add_instrument_view, name='add_instrument'),
]