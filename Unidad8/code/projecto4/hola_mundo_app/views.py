from django.shortcuts import render
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("<h1>Hola Mundo desde el curso de Abacom!</h1>")
