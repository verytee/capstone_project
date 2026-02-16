from django.urls import path
from .views import BookingList, RoomList, AboutUsView
from .views import BookingList, RoomList, PreviousBookingList


urlpatterns = [
    path('', RoomList.as_view(), name='room_list'),
    path('about/', AboutUsView.as_view(), name='about_us'),
    path('bookings/', BookingList.as_view(), name='booking_list'),
    path('manage-bookings/', BookingList.as_view(), name='manage_bookings'),
    path('previous-bookings/', PreviousBookingList.as_view(), name='previous_bookings'),
]
