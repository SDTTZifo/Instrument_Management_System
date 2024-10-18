
from django.contrib import admin
from django.urls import include, path

from Inventory.views import HomePage

urlpatterns = [
    path('', HomePage, name='index'),
    path('admin/', admin.site.urls),
    path('inventory/', include('Inventory.urls')),
    path('Booking/', include('Booking.urls')),
]