from django.http import JsonResponse
from .models import Pin
from .serializers import PinSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def pin_list(request, format=None):

    #get all pins
    #serialize
    #give return json

    if request.method == 'GET':
        pins = Pin.objects.all()
        serializer = PinSerializer(pins, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PinSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def pin_detail(request, id, format=None):
    try:
        pin = Pin.objects.get(pk = id)
    except Pin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PinSerializer(pin)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PinSerializer(pin, data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)