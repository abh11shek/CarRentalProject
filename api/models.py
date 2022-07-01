from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateField, DateTimeField

# Create your models here.

class Address(models.Model):
    address_name = models.CharField(max_length=20, null=True, default=True)
    str_add_1 = models.CharField(max_length=50)
    str_add_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin_code = models.CharField(max_length=8)

    def __str__(self):
        return self.address_name

class Branch(models.Model):
    branch_name = models.CharField(max_length=20, null=True, default=True)
    location = models.CharField(max_length=20)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.branch_name

class Car(models.Model):
    brand = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)
    model_year = models.CharField(max_length=20)
    reg_no = models.CharField(max_length=20, null=True, blank=True)
    variant = models.CharField(max_length=9) #manual/Automatic
    fuel_type = models.CharField(max_length=6) #petrol/diesel
    no_of_seats = models.IntegerField()
    odometer_reading = models.IntegerField()
    base_fare = models.IntegerField()
    hourly_charge = models.IntegerField()
    daily_charge = models.IntegerField()
    extra_charge_per_km = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.model_name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_no = models.IntegerField()
    wallet_balance = models.IntegerField()

    def __str__(self):
        return self.user.username

class Rental(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_at = DateTimeField()
    start_datetime = DateTimeField()
    return_datetime = DateTimeField()
    actual_return_time = DateTimeField(null=True, blank=True)
    distance_limit = models.IntegerField()
    distance_travelled = models.IntegerField(null=True, blank=True)
    bill_amount = models.IntegerField()
    extra_charge = models.IntegerField(null=True, blank=True)
    cancelled = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'By {self.customer.first_name} {self.customer.last_name} at {self.booked_at}'

class Stock(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    no_of_cars = models.IntegerField()

    def __str__(self):
        return f'{self.no_of_cars} vehicles'

