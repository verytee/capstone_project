from django.contrib import admin
from .models import AboutUs, ContactRequest
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(AboutUs)
class AboutUsAdmin(SummernoteModelAdmin):

    summernote_fields = ("description",)


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'created_at', 'is_resolved',)
