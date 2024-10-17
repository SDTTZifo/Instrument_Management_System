from django.db import models

class Booking(models.Model):
    equipment_category = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    maintenance_date = models.DateField(null=True, blank=True)
    booking_start_date = models.DateField()
    booking_end_date = models.DateField()
    status = models.CharField(max_length=20)
    booked_by = models.CharField(max_length=100)
    reason = models.TextField(blank=True)

    def __str__(self):
        return f"{self.equipment} booked by {self.booked_by}"