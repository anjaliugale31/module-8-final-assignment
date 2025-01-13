from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import *
from .models import Menu, Booking
from rest_framework import viewsets


def index(request):
    return render(request, 'index.html', {})

class MenuItemViews(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
