from django.urls import path
from . import views
urlpatterns=[
    path('view_near_mech',views.view_near_mech,name="view_near_mech"),
    path('view_near_pump',views.view_near_pump,name="view_near_pump"),
    path('view_near_pump',views.view_near_pump,name="view_near_pump"),
    
]