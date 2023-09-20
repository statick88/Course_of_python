# Vista en Django para mostrar la lista de tareas
from django.shortcuts import render
from .models import Tarea

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'lista_tareas.html', {'lista_tareas': tareas})

def lista_tareas2(request):
    tareas = Tarea.objects.all()
    return render(request, 'inicio.html', {'lista_tareas': tareas})

def inicio(resquest):
    return render(resquest, 'inicio.html', 'inicio')

def crear_tareas(resquest):
    return render(resquest, 'crear_tareas.html', 'crear')