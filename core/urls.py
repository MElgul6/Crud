from django.urls import path 
from .views import index, create_task, update_task, search_task, activation
from .import views

urlpatterns = [
    path('', index),
    path('new/', create_task, name='create_task'),
    path('update_task/<int:id>/', update_task, name='update_task'),
    path('search_task/', search_task, name='search_task'),
    path('activation/<int:id>/', activation, name='activation'),
    
]