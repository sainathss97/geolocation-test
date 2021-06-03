from django.contrib import admin
from django.urls import path,include
from location import views
urlpatterns = [
    path('',views.home,name='home'),
    path('my/',views.index,name='my')
]