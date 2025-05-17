from django.http import HttpResponse
from django.shortcuts import render
from appClases.models import Estudiante
from appClases.forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def inicio(request):

    # def  seleccionMateria():
    #     temasPorMateria = {
    #     "Matematicas": ["Trigonometría", "Fracciones", "Cálculo con Números Negativos"],
    #     "Circuitos Electrónicos": ["Opción 1", "Opción 2", "Opción 3"],
    #     "Técnicas Digitales": ["Opción 1", "Opción 2", "Opción 3"],
    #     "Amesea": ["Opción 1", "Opción 2", "Opción 3"],
    #     "Física": ["Opción 1", "Opción 2", "Opción 3"],
    #     "Programación en C": ["Opción 1", "Opción 2", "Opción 3"],
    #     "Programación en Python": ["Opción 1", "Opción 2", "Opción 3"]
    #     }


    # infoClase = {
    #     "Materia": "",
    #     "Tema": "",
    #     "Dia": "",
    #     "Horario": ""
    # }

    # seleccionMateria()


    dic = {}

    # incersion del html

    return render(request, "appClases/index.html")

def agenda(request):

    nombre = "Manuel"

    dic = {"nombre": nombre}

    # incersion del html

    return HttpResponse('Vista de Agenda')

# def registro(request):

#     if request.method == "POST":

#         form1 = UserRegisterForm(request.POST)

#         if form1.is_valid():

#             username = form1.cleaned_data['username']

#             form1.save()

#             return render(request, "appClases/index.html")
        
#     else:

#         form1 = UserRegisterForm()

#     return render(request, "appClases/registro.html", {"form1": form1})

# def muestraEstudiantes(request):

#     alumnos  = Estudiante.objects.all()

#     context = {"estudiantes": alumnos}

#     return render(request, "appClases/muestraAlumnos.html", context)

# def eliminaEstudiante(request, alumno_id):

#     alumnos  = Estudiante.objects.get(id=alumno_id)
#     alumnos.delete()

#     alumnos  = Estudiante.objects.all()

#     context = {"estudiantes": alumnos}

#     return render(request, "appClases/muestraAlumnos.html", context)

# def editarEstudiante(request, alumno_id):

#     alumnos  = Estudiante.objects.get(id=alumno_id)
    
#     if request.method == "POST":

#         form1 = EstudianteFormulario(request.POST)

#         if form1.is_valid():

#             info = form1.cleaned_data

#             alumnos.nombre=info['nombre']
#             alumnos.email=info['email']
#             alumnos.telefono =info['telefono']
#             alumnos.dni=info['dni']
#             alumnos.contrasenia=info['contrasenia']
            
#             alumnos.save()

#             return render(request, "appClases/index.html")
        
#     else:
#         form1 = EstudianteFormulario(initial={'nombre':alumnos.nombre,
#                                 'email':alumnos.email,
#                                 'telefono' :alumnos.telefono,
#                                 'dni':alumnos.dni,
#                                 'contrasenia':alumnos.contrasenia})

#     return render(request, "appClases/editarAlumno.html", {"form1": form1})


def inicioSesion(request):

    if request.method == 'POST':

        form = AuthenticationForm(data = request.POST)

        print(form.errors)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia  = form.cleaned_data.get('password') 

            user = authenticate(username = usuario, password = contrasenia)

            if user:

                login(request, user)

                return render(request, "appClases/index.html", {'mensaje': f"Bienvenido {user}"})

        else:

            return render(request, "appClases/iniciarSesion.html", {'mensaje': "Datos Incorrectos"})

    else:

            form = AuthenticationForm()

    return render(request, "appClases/iniciarSesion.html", {'form1': form})


#clases de vistas
#@login_required
class EstudiantesList(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = "appClases/muestraAlumnos.html"

class EstudianteCreacion(CreateView):
    model = Estudiante
    success_url  = "/AppClases/"
    fields  = ['username', 'nombre', 'email', 'telefono','contrasenia' ]

class EstudianteActualiza(UpdateView):
    model = Estudiante
    success_url  = "/AppClases/"
    fields  = ['username', 'nombre', 'email', 'telefono','contrasenia' ]

class EstudianteEliminar(DeleteView):
    model = Estudiante
    success_url  = "/AppClases/"
