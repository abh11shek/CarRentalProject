from django.urls import path
from api.views import car_views as views

urlpatterns = [
    path('', views.getCars, name='cars'),
    path('<int:pk>/', views.getCar, name='car'),
]