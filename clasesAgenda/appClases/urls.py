from django.urls import path
from appClases import views
from django.contrib.auth.views import LogoutView
# Create your views here.

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('agenda', views.agenda, name="Agenda"),
    path(r'^nuevo$', views.EstudianteCreacion.as_view() ,name="Registro"),
    path('inicioSesion', views.inicioSesion ,name="inicioSesion"),
    path('muestraAlumnos', views.EstudiantesList.as_view(), name="MuestraAlumnos"),
    path(r'^borrar/(?P<pk>\d+)$', views.EstudianteEliminar.as_view(), name="EliminarAlumno"),
    path(r'^editar/(?P<pk>\d+)$', views.EstudianteActualiza.as_view(), name="EditarAlumno"),
    path('logout', LogoutView.as_view(template_name='appClases/logout.html'), name="logout"),
] 
