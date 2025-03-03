from django.urls import path
from . import views
urlpatterns=[
    path('view_near_mech',views.view_near_mech,name="view_near_mech"),
    path('view_near_pump',views.view_near_pump,name="view_near_pump"),
    path('view_details/<int:id>/',views.view_details,name="view_details"),
    path('view_pumbdetails/<int:id>/',views.view_pumbdetails,name="view_pumbdetails"),
    path('mechbooking/<int:id>/',views.booking,name="mechbooking"),
    path('pumbbooking/<int:id>/',views.pumb_booking,name="pumbbooking"),
    path('view_mech_bookings',views.view_mech_bookings,name="view_mech_bookings"),
    path('view_pumb_bookings',views.view_pumb_bookings,name="view_pumb_bookings"),
    path('add_mech_feedback/<int:id>/', views.add_mech_feedback, name='add_mech_feedback'),
    path('view_mech_feedback/<int:id>/', views.view_mech_feedback, name='view_mech_feedback'),
    path('add_petrol_feedback/<int:id>/', views.add_petrol_feedback, name='add_petrol_feedback'),
    path('view_petrol_feedback/<int:id>/', views.view_petrol_feedback, name='view_petrol_feedback'),
]