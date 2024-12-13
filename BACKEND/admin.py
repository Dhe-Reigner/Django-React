from django.contrib import admin
from .models import Room, RoomImage,OccupiedDate



# Register your models here.
admin.site.register(Room)
admin.site.register(RoomImage)
admin.site.register(OccupiedDate)