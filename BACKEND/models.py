from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Room(models.Model):
    ROOM_TYPES = [
        ('standard', 'Standard Room'),
        ('deluxe', 'Deluxe Room'),
        ('suite', 'Suite')
    ]
    CURRENCY_TYPES = [
        ('USD', 'USD'),
        ('EUR', 'EUR')
    ]
    
  
    name = models.CharField(max_length=200, blank=True,default='')
    type = models.CharField(max_length=200, choices=ROOM_TYPES, default='standard')
    pricePerNight = models.IntegerField(default=150)
    currencyType = models.CharField(max_length=200, choices=CURRENCY_TYPES, default='USD')
    maxOccupancy = models.IntegerField(default=2)
    description = models.TextField(blank=True, default='')
    # image = models.ImageField(upload_to='room_images/', blank=True)
    isAvailable = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.name} ({self.type})'
    
    
class RoomImage(models.Model):
    image = models.ImageField(upload_to="room_images/")
    caption = models.CharField(max_length=255, blank=True,null=True)
    room = models.ForeignKey(Room,related_name="images",on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Image for {self.room.name} - {self.caption or 'No Caption'}"
    
class OccupiedDate(models.Model):
    room = models.ForeignKey(Room, related_name="occupied_dates", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="booked_dates",default='', on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return f"{self. date} - {self.room.name} booked by {self.user.username}"
    
class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, blank=True)
    
    