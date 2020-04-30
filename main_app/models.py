from django.db import models
from django.urls import reverse
from datetime import date

class Trip(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    arrival = models.DateField('Arrival Date')
    departure = models.DateField('Departure Date')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'trip_id': self.id})