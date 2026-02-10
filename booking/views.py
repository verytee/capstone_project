from operator import add
from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Room, RoomBooking

# Create your views here.

class RoomList(generic.ListView):
    model = Room
    template_name = 'booking/index.html'
    paginate_by = 6

# add logic so dates in the past are not shown as available for booking

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now().date()
        return context


class BookingList(generic.ListView):
    model = RoomBooking
    template_name = 'booking/manage-booking.html'