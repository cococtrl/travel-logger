from django.db import models
from django.urls import reverse
from datetime import date

TICKETS = (
    ('Y', 'Purchased'),
    ('N', 'Not Purchased'),
    ('NA', 'Not Needed'),
)

class Trip(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    arrival = models.DateField('Arrival Date')
    departure = models.DateField('Departure Date')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'trip_id': self.id})

class Activity(models.Model):
    date = models.DateField()
    activity = models.CharField(max_length=50)
    tickets = models.CharField(
        max_length=2,
        choices=TICKETS,
        default=TICKETS[0][0])
    
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_tickets_display()} on {self.date}"

    class Meta:
        ordering = ['-date']