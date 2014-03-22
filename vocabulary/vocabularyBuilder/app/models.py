# encoding:utf-8
from django.db import models
import datetime
# Create your models here.

class Diccionario(models.Model):
    nombre = models.CharField(max_length=70)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.nombre


class Palabra(models.Model):
    diccionario = models.ForeignKey(Diccionario)
    palabra_A = models.CharField(max_length=128)
    palabra_B = models.CharField(max_length=128)
    fecha = models.DateField('ultima revision')
    dias_nuevo_intento = models.IntegerField()
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.palabra_A


class Dia(models.Model):
    # En esta clase almaceno cada día jugado para luego poder calcular si
    # han pasado los días necesarios para mostrar palabra nuevamente en el juego
    dia_jugado = models.DateField('Dia jugado') 

    def __unicode__(self):
        return str(self.dia_jugado)
