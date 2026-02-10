from django.contrib import admin
from .models import Room, RoomBooking
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(RoomBooking)

@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)