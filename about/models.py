from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class AboutUs(models.Model):
    """
    Model to store information about the hotel for the About Us page.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title