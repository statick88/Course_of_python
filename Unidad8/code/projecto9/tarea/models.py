from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    # Agregar campos para actualización y eliminación
    fecha_actualizacion = models.DateTimeField(auto_now=True)
