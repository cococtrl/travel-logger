from django.db import models
from django.urls import reverse
from datetime import date

TICKETS = (
    ('Y', 'Purchased'),
    ('N', 'Not Purchased'),
    ('NA', 'Not Needed'),
)

class Landmark(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

class Trip(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    arrival = models.DateField('Arrival Date')
    departure = models.DateField('Departure Date')
    landmarks = models.ManyToManyField(Landmark)

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

class Photo(models.Model):
    url = models.CharField(max_length=200)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for trip_id: {self.trip_id} @{self.url}"