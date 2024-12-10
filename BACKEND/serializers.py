from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model : Room
        fields : ['url','id','name','type','pricePerNight','currencyType','maxOccupancy','description']