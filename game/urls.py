from django.urls import path
from . import views

urlpatterns = [
    path('', views.opens),
    path('opens/', views.index),
]