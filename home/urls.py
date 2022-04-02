from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.index, name ='Home'),
    path('res/',views.data, name="data"),
    path('res/index/',views.index, name ='Home'),
]
