# encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Diccionario(models.Model):
    nombre = models.CharField(max_length=100)
    jugada = models.IntegerField()
    usuario = models.ForeignKey(User)
    fecha_ultima_jugada = models.DateField(auto_now_add=True)
    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s - %s" % (self.nombre, self.usuario)


class Palabra(models.Model):
    diccionario = models.ForeignKey(Diccionario)
    palabra_A = models.CharField(max_length=140)
    palabra_B = models.CharField(max_length=140)
    jugada_proxima = models.IntegerField(default=1)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s - %s" % (self.palabra_A, self.palabra_B)
    def __str__(self):  # Python 3: def __str__(self):
        return "%s - %s" % (self.palabra_A, self.palabra_B)
