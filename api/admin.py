from django.contrib import admin
from .models import Address, Branch, Car, Customer, Rental, Stock

# Register your models here.
admin.site.register(Address)
admin.site.register(Branch)
admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Rental)
admin.site.register(Stock)