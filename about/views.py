from django.shortcuts import render, redirect
from .models import AboutUs
from .forms import ContactRequestForm
from django.contrib import messages

# Create your views here.


def about_us(request):
    # Display on the about page
    about_info = AboutUs.objects.first()
    contact_form = ContactRequestForm()

    if request.method == "POST":
        contact_form = ContactRequestForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            contact_form = ContactRequestForm()  # Reset the form after saving
            messages.add_message(
                request, messages.SUCCESS, "Your message has been sent successfully. Our team will get back to you shortly.")
            return redirect("about_us")
        else:
            messages.add_message(request, messages.ERROR, "There was an error sending your message. Please try again.")
            return redirect("about_us")

    return render(
        request,
        "about/about.html",
        {
            "about_info": about_info,
            "contact_form": contact_form
            },
    )
