from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

from .models import Trip
from .forms import ActivityForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def trips_index(request):
    trips = Trip.objects.all()
    return render(request, 'trips/index.html', {'trips': trips })

def trips_detail(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    activity_form = ActivityForm()
    return render(request, 'trips/detail.html', { 
            'trip': trip,
            'activity_form' : activity_form
        })

def add_activity(request, trip_id):
    form = ActivityForm(request.POST)
    if form.is_valid():
        new_activity = form.save(commit=False)
        new_activity.trip_id = trip_id
        new_activity.save()
        
    return redirect('detail', trip_id=trip_id)

class TripCreate(CreateView):
    model = Trip
    fields = '__all__'
    success_url= '/trips/'

class TripUpdate(UpdateView):
    model = Trip
    fields = ['description', 'arrival', 'departure']

class TripDelete(DeleteView):
    model = Trip
    success_url = '/trips/'

