from django.urls import path
from api.views import booking_views as views

urlpatterns = [
    path('', views.getBookings, name='bookings'),
    path('<int:pk>', views.getBookingById, name='booking'),
    path('add/', views.addBooking, name='add-booking'),
    path('cancel/', views.cancelBooking, name='complete-booking'),
]