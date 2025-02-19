from django.urls import path
from . import views
urlpatterns=[
    path('view_near_mech',views.view_near_mech,name="view_near_mech"),
    path('view_near_pump',views.view_near_pump,name="view_near_pump"),
    path('view_details/<int:id>/',views.view_details,name="view_details"),
    path('mechbooking/<int:id>/',views.booking,name="mechbooking"),
    path('bookings',views.view_booking,name="bookings"),
    path('approve_booking/<int:id>/',views.approve_booking,name="approve_booking"),
    path('reject_booking/<int:id>/',views.reject_booking,name="reject_booking"),
    path('update_status/<int:id>/',views.update_status,name="update_status"),
    
]