from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from rest_framework import status

from api.models import Car
from api.serializers import CarSerializer

# Create your views here.

@api_view(['GET'])
def getCars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCar(request, pk):
    car = Car.objects.get(id=pk)
    serializer = CarSerializer(car, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getCars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCar(request, pk):
    car = Car.objects.get(id=pk)
    serializer = CarSerializer(car, many=False)
    return Response(serializer.data)