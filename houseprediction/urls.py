from django.urls import path, include
from .import views

# app_name ='fyp'

urlpatterns = [
    path('',views.index, name="index"),
    path('about_us',views.about_us, name="about_us"),
    path('result',views.result, name="result"),
    


    
]
