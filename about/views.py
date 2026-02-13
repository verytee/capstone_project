from django.shortcuts import render
from .models import AboutUs

# Create your views here.

def about_us(request):
# View to display the About Us page with hotel information.
    about_info = AboutUs.objects.first()
    return render(request, 'about/about-us.html', 
                  {'about_info': about_info})
