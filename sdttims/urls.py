
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Inventory/', include('Inventory.urls')),   
    path('Booking/', include('Booking.urls')),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
