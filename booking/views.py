from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Room, RoomBooking
from datetime import datetime

# Create your views here.


class RoomList(generic.ListView):
    model = Room
    template_name = 'booking/index.html'

class BookingList(LoginRequiredMixin, generic.ListView):
    model = RoomBooking
    template_name = 'booking/manage-booking.html'

    def get_queryset(self):
        return RoomBooking.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")
        next_url = request.POST.get("next") or "manage_bookings"

        if action == "update":
            booking = get_object_or_404(
                RoomBooking,
                id=request.POST.get("booking_id"),
                user=request.user
            )
            booking.check_in = datetime.strptime(
                request.POST.get("check_in_date"),
                "%Y-%m-%d"
            ).date()
            booking.no_of_nights = int(request.POST.get("number_of_nights"))
            booking.save()
            return redirect(next_url)

        if action == "delete":
            booking = get_object_or_404(
                RoomBooking,
                id=request.POST.get("booking_id"),
                user=request.user
            )
            booking.delete()
            return redirect(next_url)

        room = get_object_or_404(Room, id=request.POST.get("room_id"))
        try:
            check_in_date = datetime.strptime(
                request.POST.get("check_in_date"),
                "%Y-%m-%d"
            ).date()
            nights = int(request.POST.get("number_of_nights"))
        except (TypeError, ValueError):
            return redirect(next_url)

        RoomBooking.objects.create(
            user=request.user,
            room=room,
            check_in=check_in_date,
            no_of_nights=nights
        )
        return redirect(next_url)
