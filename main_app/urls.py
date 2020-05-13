from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trips/', views.trips_index, name='index'),
    path('trips/<int:trip_id>/', views.trips_detail, name='detail'),
    path('trips/<int:trip_id>/add_activity/', views.add_activity, name='add_activity'),
    path('trips/create/', views.TripCreate.as_view(), name='trips_create'),
    path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trips_update'),
    path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trips_delete'),
    path('landmarks/', views.LandmarkList.as_view(), name="landmarks_index"),
    path('landmarks/<int:pk>/', views.LandmarkDetail.as_view(), name='landmarks_detail'),
    path('landmarks/<int:pk>/update/', views.LandmarkUpdate.as_view(), name='landmarks_update'),
    path('landmarks/<int:pk>/delete/', views.LandmarkDelete.as_view(), name='landmarks_delete'),
    path('landmarks/create/', views.LandmarkCreate.as_view(), name='landmarks_create'),
    path('trips/<int:trip_id>/assoc_landmark/<int:landmark_id>/', views.assoc_landmark, name='assoc_landmark'),
    path('trips/<int:trip_id>/add_photo/', views.add_photo, name='add_photo')
]