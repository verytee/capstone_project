from django.contrib import admin
from django.utils import timezone
from django_summernote.admin import SummernoteModelAdmin
from .models import Room, RoomBooking


# Register your models here.
class BookingStatusFilter(admin.SimpleListFilter):
    title = "Booking status"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return [
            ("past", "Past"),
            ("upcoming", "Upcoming or today"),
        ]

    def queryset(self, request, queryset):
        today = timezone.now().date()
        if self.value() == "past":
            return queryset.filter(check_in__lt=today)
        if self.value() == "upcoming":
            return queryset.filter(check_in__gte=today)
        return queryset


@admin.register(RoomBooking)
class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ("user", "room", "check_in", "no_of_nights")
    list_filter = (BookingStatusFilter, "check_in")


@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):
    summernote_fields = ("description",)
