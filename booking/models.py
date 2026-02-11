from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.


class Room(models.Model):
    """
    Model to store available rooms for booking.
    """
    type = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['type']

    def __str__(self):
        return self.type


class RoomBooking(models.Model):
    """
    Model to store user bookings for rooms.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    no_of_nights = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.room.type} ({self.check_in})"

    def clean(self):
        if self.check_in and self.check_in < timezone.now().date():
            raise ValidationError({"check_in": "The check-in date cannot be in the past."})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
