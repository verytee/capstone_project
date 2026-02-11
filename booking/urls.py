from django.urls import path
from .views import BookingList, RoomList


urlpatterns = [
    path('', RoomList.as_view(), name='room_list'),
    path('bookings/', BookingList.as_view(), name='booking_list'),
    path('manage-bookings/', BookingList.as_view(), name='manage_bookings'),
]
