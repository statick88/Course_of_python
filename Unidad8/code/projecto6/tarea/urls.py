# En el archivo urls.py de la aplicación Django
from django.urls import path
from . import views

urlpatterns = [
    path('tareas/', views.lista_tareas, name='lista_tareas'),
]