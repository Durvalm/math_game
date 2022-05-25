from django.urls import path
from . import views

urlpatterns = [
    path('', views.math, name='math'),
    path('operation', views.operation, name='operation'),

]