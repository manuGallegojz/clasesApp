from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

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

    return render(request, "appClases/about.html")

def registro(request):

    return HttpResponse('Vista de registro')