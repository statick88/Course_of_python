from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('lista_tareas/', views.lista_tareas, name='lista_tareas'),
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
    path('detalle_tarea/<int:pk>/', views.detalle_tarea, name='detalle_tarea'),
    path('editar_tarea/<int:pk>/', views.editar_tarea, name='editar_tarea'),  # Nueva URL
    path('eliminar_tarea/<int:pk>/', views.eliminar_tarea, name='eliminar_tarea'),  # Nueva URL
]
