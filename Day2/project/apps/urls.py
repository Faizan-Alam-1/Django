from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home , name='home' ),
    path('index/<str:pk>', views.index, name='index' ),
    path('addProject', views.project_form, name='addProject' ),
    path('update_form/<str:pk>', views.update_form, name='update_form' ),
    path('delete_form/<str:pk>', views.delete_form, name='delete_form' ),

]
