from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework import generics
from .serializers import *
from .models import Menu, Booking
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import response



def index(request):
    return render(request, 'index.html', {})

class MenuItemViews(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return response({"message":"This view is protected"})
