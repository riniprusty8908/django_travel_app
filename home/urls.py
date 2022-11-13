
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('link',views.link,name='link'),
    path('trips',views.trips,name='trips'),
    path('stays',views.stays,name='stays'),
    path('contact',views.contact,name='trips'),
    ]
   
   
