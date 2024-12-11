from rest_framework import serializers
from .models import Room,RoomImage




class RoomImageSerializer(serializers.HyperlinkedModelSerializer):
    room = serializers.HyperlinkedRelatedField(
        view_name = 'room-detail',
        queryset = Room.objects.all())
    class Meta:
        model = RoomImage
        fields = ['url','id','image','caption','room']
        
        
         
class RoomSerializer(serializers.ModelSerializer):
    images = serializers.HyperlinkedRelatedField(
        view_name = 'roomimage-detail',
        many=True,
        read_only=True)
    class Meta:
        model = Room
        fields = ['url','id','name','type','pricePerNight','currencyType','maxOccupancy','description','images']
        #fields = '__all__' 
        

    