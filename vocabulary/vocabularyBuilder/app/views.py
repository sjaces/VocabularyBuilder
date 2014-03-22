from django.shortcuts import render

from app.models import Diccionario, Palabras, Dia
from django.shortcuts import render_to_response
# Create your views here.

def lista_palabras(request):
    todas_palabras = Palabras.objects.all()
    return render_to_response('lista_palabras.html',{'lista':todas_palabras})
