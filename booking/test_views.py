from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

from about import models
from .models import Room, RoomBooking


class TestBookingViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.room = Room.objects.create(
            type="Test Room",
            subtitle="Test Room Subtitle",
            description="Test room description",
            featured_image="placeholder"
        )
        self.booking = RoomBooking.objects.create(
            user=self.user,
            room=self.room,
            check_in="2027-01-01",
            no_of_nights=1
        )
