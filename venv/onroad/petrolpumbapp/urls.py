from django.urls import path
from . import views
urlpatterns=[
    path('my_bookings',views.view_pumbbooking,name="my_bookings"),
    
    path('pumb_approve_booking/<int:id>/',views.pumb_approve_booking,name="pumb_approve_booking"),
    
    path('pumb_reject_booking/<int:id>/',views.pumb_reject_booking,name="pumb_reject_booking"),
    
    path('pumb_update_status/<int:id>/',views.pumb_update_status,name="pumb_update_status"),
]
