from django.db import models

class Instrument(models.Model):
    instrument_name = models.CharField(max_length=100)
    instrument_description = models.TextField()
    owned_by = models.CharField(max_length=100)

    def __str__(self):
        return self.instrument_name