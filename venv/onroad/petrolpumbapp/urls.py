from django.urls import path
from . import views
urlpatterns=[
    path('bookings_pumb',views.view_pumbbooking,name="bookings_pumb"),
    
    path('pumb_approve_booking/<int:id>/',views.pumb_approve_booking,name="pumb_approve_booking"),
    
    path('pumb_reject_booking/<int:id>/',views.pumb_reject_booking,name="pumb_reject_booking"),
    
    path('pumb_update_status/<int:id>/',views.pumb_update_status,name="pumb_update_status"),

    path('assign_delivery_agent/<int:booking_id>/', views.assign_delivery_agent, name='assign_delivery_agent'),

    path('delivery_agent_bookings',views.delivery_agent_bookings,name="delivery_agent_bookings"),
    
    path('petrol-pump/', views.petrol_pump_dashboard, name='petrol_pump_dashboard'),
    
    path('add_fuel_detail', views.add_fuel_detail, name='add_fuel_detail'),
    
    path('view_fuel_details', views.view_fuel_details, name='view_fuel_details'),
    path('delete_fuel/<int:id>/', views.delete_fuel, name='delete_fuel'),
    path('view_petrol_feedbacks/', views.view_petrol_feedbacks, name='view_petrol_feedbacks'),


]
