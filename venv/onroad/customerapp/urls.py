from django.urls import path
from . import views
urlpatterns=[
    path('view_near_mech',views.view_near_mech,name="view_near_mech"),
    path('view_near_pump',views.view_near_pump,name="view_near_pump"),
    path('view_details/<int:id>/',views.view_details,name="view_details"),
    path('view_pumbdetails/<int:id>/',views.view_pumbdetails,name="view_pumbdetails"),
    path('mechbooking/<int:id>/',views.booking,name="mechbooking"),
    path('pumbbooking/<int:id>/',views.pumb_booking,name="pumbbooking"),
    path('bookings',views.view_booking,name="bookings"),
    path('bookings',views.view_pumbbooking,name="bookings"),
    path('approve_booking/<int:id>/',views.approve_booking,name="approve_booking"),
    path('pumb_approve_booking/<int:id>/',views.pumb_approve_booking,name="pumb_approve_booking"),
    path('reject_booking/<int:id>/',views.reject_booking,name="reject_booking"),
    path('pumb_reject_booking/<int:id>/',views.pumb_reject_booking,name="pumb_reject_booking"),
    path('update_status/<int:id>/',views.update_status,name="update_status"),
    path('update_status/<int:id>/',views.pumb_update_status,name="update_status"),
    
]