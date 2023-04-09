from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('testing/', views.testing, name='testing'),
    path('', views.main, name='main'),
    path('members/details/<int:id>', views.details, name ='details' )
    
]
