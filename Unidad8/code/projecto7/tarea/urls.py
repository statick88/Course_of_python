from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('tareas/', views.lista_tareas, name='lista_tareas'),
    path('tareas_2/', views.lista_tareas2, name='lista_tareas'),
    path('tareas_3/', views.crear_tareas, name='crear_tareas'),
]