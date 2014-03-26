#encoding:utf-8
from django import forms
from django.forms import ModelForm
from models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import *

class DiccionarioForm(forms.ModelForm):
    class Meta:
        model = Diccionario
    
class PalabraForm(ModelForm):
    class Meta:
        model = Palabra
        exclude = ("diccionario", "jugada_proxima")
