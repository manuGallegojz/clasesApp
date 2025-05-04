from django.urls import path
from appClases import views

# Create your views here.

urlpatterns = [
    path('', views.inicio),
    path('agenda', views.agenda)
] 
