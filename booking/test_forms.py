from datetime import timedelta
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from .models import Room, RoomBooking


class RoomBookingModelTest(TestCase):
    def test_valid_booking(self):
        user = User.objects.create_user(username="testuser", password="pass12345")
        room = Room.objects.create(
            type="Double Room",
            subtitle="Test subtitle",
            description="Test description"
        )
        booking = RoomBooking(
            user=user,
            room=room,
            check_in=timezone.now().date() + timedelta(days=1),
            no_of_nights=3
        )

        self.assertIsNone(booking.full_clean())