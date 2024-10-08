
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('Inventory.urls')),
    path('Booking/', include('Booking.urls')),
]