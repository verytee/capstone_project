from django.shortcuts import render
from .models import AboutUs
from .forms import ContactRequestForm

# Create your views here.

def about_us(request):
# Display on the about page
    about_info = AboutUs.objects.first()
    contact_form = ContactRequestForm()

    return render(
        request,
        "about/about.html", 
        {
            "about_info": about_info, 
            "contact_form": contact_form
            },
    )
