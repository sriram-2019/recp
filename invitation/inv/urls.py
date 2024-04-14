from django.contrib import admin
from django.urls import path,include
from inv import views

urlpatterns = [
    path('',views.index,name="")
]