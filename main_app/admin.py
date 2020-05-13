from django.contrib import admin
from .models import Trip, Activity, Landmark, Photo
# Register your models here.

admin.site.register(Trip)
admin.site.register(Activity)
admin.site.register(Landmark)
admin.site.register(Photo)