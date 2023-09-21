# Creación de una vista para listar, crear y actualizar tareas
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarea
from .forms import TareaForm
from rest_framework import generics
from .models import Tarea
from .serializers import TareaSerializer

def lista_tareas(request):
    tareas = Tarea.objects.all()  # Cambiar 'tarea' a 'tareas'
    return render(request, 'lista_tareas.html', {'tareas': tareas})  # Cambiar 'lista_tarea' a 'tareas'

def crear_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save()
            return redirect('detalle_tarea', pk=tarea.pk)
    else:
        form = TareaForm()
    return render(request, 'crear_tarea.html', {'form': form})

def detalle_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    return render(request, 'detalle_tarea.html', {'tarea': tarea})

def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            tarea = form.save()
            return redirect('detalle_tarea', pk=tarea.pk)
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'editar_tarea.html', {'form': form, 'tarea': tarea})

def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == "POST":
        tarea.delete()
        return redirect('lista_tareas')
    return render(request, 'eliminar_tarea.html', {'tarea': tarea})

class ListaTareasAPI(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class DetalleTareaAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer