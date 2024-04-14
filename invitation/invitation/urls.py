from django.contrib import admin
from django.urls import path,include
from inv import urls

urlpatterns = [
   path("",include('inv.urls')),
]