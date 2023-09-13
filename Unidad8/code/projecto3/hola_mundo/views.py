# En el archivo views.py de la aplicación Django
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("¡Hola Mundo en el curso de Abacom!")