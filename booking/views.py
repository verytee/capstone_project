from django.shortcuts import render
from django.views import generic
from .models import Room, RoomBooking

# Create your views here.

class RoomList(generic.ListView):
    model = Room


class BookingList(generic.ListView):
    model = RoomBooking
    template_name = 'booking/booking-list.html'