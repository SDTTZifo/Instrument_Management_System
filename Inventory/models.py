from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    category_description = models.TextField()    

    def __str__(self):
        return self.category_name

class Instrument(models.Model):    
    instrument_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, null=True)
    model_number = models.CharField(max_length=100, null=True)
    manufacturer = models.CharField(max_length=100, null=True)
    purchased_On =models.DateField(null=True)
    owned_by = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    maintenance_date = models.DateField(null=True)   

    def __str__(self):
        return self.instrument_name