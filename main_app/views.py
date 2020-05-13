from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView

from .models import Trip, Landmark
from .forms import ActivityForm

import uuid
import boto3
S3_BASE_URL = 'https://s3-us-east-1.amazonaws.com/'
BUCKET = 'travellogger'


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
    nearby_landmarks = Landmark.objects.exclude(id__in = trip.landmarks.all().values_list('id'))
    return render(request, 'trips/detail.html', { 
            'trip': trip,
            'activity_form' : activity_form,
            'landmarks' : nearby_landmarks
        })

def add_activity(request, trip_id):
    form = ActivityForm(request.POST)
    if form.is_valid():
        new_activity = form.save(commit=False)
        new_activity.trip_id = trip_id
        new_activity.save()
        
    return redirect('detail', trip_id=trip_id)

def assoc_landmark(request, trip_id, landmark_id):
    Trip.objects.get(id=trip_id).landmarks.add(landmark_id)
    return redirect('detail', trip_id=trip_id)

def add_photo(request, trip_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, trip_id=trip_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
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

class LandmarkList(ListView):
    model = Landmark

class LandmarkDetail(DeleteView):
    model = Landmark

class LandmarkCreate(CreateView):
    model = Landmark
    fields = ['name']
    success_url = '/landmarks/'

class LandmarkUpdate(UpdateView):
    model = Landmark
    fields = ['name']
    success_url = '/landmarks/'

class LandmarkDelete(DeleteView):
    model = Landmark
    success_url = '/landmarks/'