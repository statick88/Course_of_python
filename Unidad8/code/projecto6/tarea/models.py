# Definición de un modelo para crear Tareas en Django
from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripción = models.TextField()
    fecha_creación = models.DateTimeField('fecha de creación')

    def __str__(self):
        return self.titulo