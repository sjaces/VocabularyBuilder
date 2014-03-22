# encoding: utf-8
from django.shortcuts import render

from app.models import Diccionario, Palabra, Dia
from django.shortcuts import render_to_response
# Create your views here.

def lista(request):
    todas_palabras = Palabra.objects.all()
    mensaje ="© 2014 by sjaces"
    dias = Dia.objects.all()
    return render_to_response('lista.html',{'lista':todas_palabras, 
        'hola':mensaje, 'todos_los_dias': dias})
