from django.urls import path
from . import views
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('lista_tareas/', views.lista_tareas, name='lista_tareas'),
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
    path('detalle_tarea/<int:pk>/', views.detalle_tarea, name='detalle_tarea'),
    path('editar_tarea/<int:pk>/', views.editar_tarea, name='editar_tarea'),  # Nueva URL
    path('eliminar_tarea/<int:pk>/', views.eliminar_tarea, name='eliminar_tarea'),  # Nueva URL

    path('api/tareas/', views.ListaTareasAPI.as_view(), name='lista_tareas_api'),
    path('api/tareas/<int:pk>/', views.DetalleTareaAPI.as_view(), name='detalle_tarea_api'),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
