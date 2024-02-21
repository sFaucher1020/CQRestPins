from rest_framework import serializers
from .models import Pin

class PinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pin
        fields = ['id','user','pinName','pinDesc','pinLat','pinLong']