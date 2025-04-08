
from django.contrib import admin
from django.urls import path , include
from courses.views.homepage import home




urlpatterns = [
    path('', home , name="home page"),
    
]