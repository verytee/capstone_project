from datetime import timedelta
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from .models import Room, RoomBooking


class RoomBookingModelTest(TestCase):
    def test_valid_booking(self):
        user = User.objects.create_user(
            username="testuser", password="pass12345")
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

    def test_booking_with_past_check_in_date(self):
        user = User.objects.create_user(
            username="testuser", password="pass12345")
        room = Room.objects.create(
            type="Double Room",
            subtitle="Test subtitle",
            description="Test description"
        )
        booking = RoomBooking(
            user=user,
            room=room,
            check_in=timezone.now().date() - timedelta(days=1),
            no_of_nights=3
        )

        with self.assertRaises(Exception) as context:
            booking.full_clean()
        self.assertIn("The check-in date cannot be in the past.", str(context.exception))

    def test_booking_with_zero_nights(self):
        user = User.objects.create_user(
            username="testuser", password="pass12345")
        room = Room.objects.create(
            type="Double Room",
            subtitle="Test subtitle",
            description="Test description"
        )
        booking = RoomBooking(
            user=user,
            room=room,
            check_in=timezone.now().date() + timedelta(days=1),
            no_of_nights=0
        )

        with self.assertRaises(Exception) as context:
            booking.full_clean()
        self.assertIn("Ensure this value is greater than or equal to 1.", str(context.exception))