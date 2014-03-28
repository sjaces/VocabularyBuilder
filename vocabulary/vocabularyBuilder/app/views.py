# encoding: utf-8
from django.http import HttpResponseRedirect
from app.models import *
from app.forms import *
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import *
from django.template import RequestContext
from datetime import datetime
import random

# Create your views here.

def lista(request):
    todas_palabras = Palabra.objects.all()
    mensaje ="© 2014 by sjaces"
    # return render_to_response('lista.html',{'lista':todas_palabras, 
    #     'hola':mensaje, 'todos_los_dias': dias})
    return render_to_response('lista.html', locals())

def home(request):
    # mi_usuario = request.user
    todos_diccionarios = Diccionario.objects.all()
    # unos_diccionarios = Diccionario.objects.filter( usuario=request.user)
    if request.user.is_authenticated():
        # Do something for authenticated users.
        mi_usuario = request.user
        mis_diccionarios = get_list_or_404(todos_diccionarios, usuario = mi_usuario)
    # else:
        # Do something for anonymous users.
        # mi_usuario = 'no'

    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

@login_required
def nueva_palabra(request, id_diccionario):
    mi_diccionario = Diccionario.objects.get(pk = id_diccionario)
    if request.method=='POST':
        formulario = PalabraForm(request.POST)
        if formulario.is_valid():
            nueva_palabra=formulario.save(commit=False)
            nueva_palabra.diccionario = mi_diccionario
            nueva_palabra.save()
            return HttpResponseRedirect('/')
    else:
        formulario = PalabraForm()
    return render_to_response('nueva_palabra.html',{'formulario':formulario, 'mi_diccionario': mi_diccionario}, context_instance=RequestContext(request))


@login_required
def jugar(request, id_diccionario):
    respuesta = "No hay respusta"
    mi_usuario = request.user
    todos_diccionarios = Diccionario.objects.all()
    mis_diccionarios = get_list_or_404(todos_diccionarios, usuario = mi_usuario)
    # mi_diccionario = Diccionario.objects.get(pk = id_diccionario)
    mi_diccionario = get_object_or_404(todos_diccionarios, pk = id_diccionario)
    hoy = datetime.today()

    #Compruebo si se ha contestado una palabra y actuo en consecuencia
    if request.method == 'POST':
        respuesta = request.POST.get("respuesta")
        pregunta = request.POST.get("pregunta")
        id_palabra = request.POST.get("id")
        palabra_jugada = Palabra.objects.get(pk = id_palabra)
        if palabra_jugada.palabra_B == respuesta:
            resultado = "correcto"
            return render_to_response('jugar.html', locals(), context_instance=RequestContext(request))
    
    # Si es la primera vez que se juega este diccionario hoy, se actualiza su estado para que cuente como día jugado
    if mi_diccionario.fecha_ultima_jugada <  hoy.date():
        mi_diccionario.jugada += 1
        mi_diccionario.fecha_ultima_jugada = hoy.date()
        mi_diccionario.save()

    # Preparo una palabra entres las válidas para jugar
    mis_palabras = Palabra.objects.filter(diccionario = mi_diccionario).filter(jugada_proxima__lte=mi_diccionario.jugada)
    # mis_palabras = Palabra.get_list_or_404(mi_diccionario, jugada_proxima__lte=mi_diccionario.jugada)
    numero_aleatorio = random.randint(0, len(mis_palabras)-1)
    palabra_juego = mis_palabras[numero_aleatorio]
    # palabras = get_object_or_404(diccionarios, pk=id_diccionario)
    return render_to_response('jugar.html', locals(), context_instance=RequestContext(request))

@login_required
def reprogramar(request):
    if request.method == 'POST':
        dias = int(request.POST.get("dias"))
        id_palabra = request.POST.get("id")
        palabra_jugada = Palabra.objects.get(pk = id_palabra)
        id_diccionario = palabra_jugada.diccionario.pk
        palabra_jugada.jugada_proxima = dias + Diccionario.objects.get(pk=id_diccionario).jugada
        palabra_jugada.save()
        # return render_to_response('jugar.html', locals(), context_instance=RequestContext(request))
        return HttpResponseRedirect("/jugar/%s" % id_diccionario)
    else:
        return HttpResponseRedirect("/")



@login_required
def salir(request):
    logout(request)
    # return render_to_response('index.html', locals())
    return HttpResponseRedirect("/")
