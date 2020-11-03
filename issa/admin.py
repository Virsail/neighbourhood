from django.contrib import admin
from .models import NeighbourHood, Profile, Business, Activity

# Register your models here.
admin.site.register(NeighbourHood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Activity)
