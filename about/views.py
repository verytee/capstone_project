from django.shortcuts import render
from .models import AboutUs

# Create your views here.

def about_us(request):
# Display on the about page
    about_info = AboutUs.objects.first()
    return render(request, "about/about.html", {"about_info": about_info})
