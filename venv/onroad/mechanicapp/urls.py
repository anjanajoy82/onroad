from django.urls import path
from . import views
urlpatterns=[
    path('bookings',views.view_booking,name="bookings"),
    path('approve_booking/<int:id>/',views.approve_booking,name="approve_booking"),
    path('reject_booking/<int:id>/',views.reject_booking,name="reject_booking"),
    path('mech_update_status/<int:id>/',views.mech_update_status,name="mech_update_status"),
]