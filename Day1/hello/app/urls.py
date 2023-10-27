
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home),
     path('contact/<str:pk>' , views.contact , name = 'contact')   
]