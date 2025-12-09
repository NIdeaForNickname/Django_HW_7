from django.urls import path
from . import views

urlpatterns = [
    path('add_event/', views.create_event, name='add'),
    path('event/', views.view_event, name='event'),
]