# Vista en Django para mostrar la lista de tareas
from django.shortcuts import render
from .models import Tarea

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'lista_tareas.html', {'lista_tareas': tareas})