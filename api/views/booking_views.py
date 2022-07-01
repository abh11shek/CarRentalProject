from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
import datetime, time 

from rest_framework import status

from api.models import Car, Rental, Branch
from api.serializers import CarSerializer, BookingSerializer

@api_view(['POST'])
def addBooking(request):
    user = request.user
    data = request.data

    branch = Branch.objects.get(branch_name='Bengaluru')
    car = Car.objects.get(id=data['carId'])

    booking = Rental.objects.create(
        customer=user,
        branch=Branch.objects.get(id=data['branchId']),
        car=Car.objects.get(id=data['carId']),
        booked_at=datetime.datetime.now(),
        start_datetime=datetime.datetime.fromtimestamp(int(data['startDateTime'])/1000),
        return_datetime=datetime.datetime.fromtimestamp(int(data['returnDateTime'])/1000),
        distance_limit=data['distanceLimit'],
        bill_amount=data['billAmount']
    )

    booking.save()

    serializer = BookingSerializer(booking, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def cancelBooking(request):
    data = request.data

    Rental.objects.filter(id=data['booking_id']).update(
        cancelled = True
    )

    booking = Rental.objects.all()
    serializer = BookingSerializer(booking, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBookings(request):
    booking = Rental.objects.all()
    serializer = BookingSerializer(booking, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBookingById(request, pk):
    booking = Rental.objects.get(id=pk)
    serializer = BookingSerializer(booking, many=False)
    return Response(serializer.data)