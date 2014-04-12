from app.models import *
from datetime import *
# from django.utils.encoding import *

def dic(id_diccionario):
    f = open("pruebas.ltm")
    g = open("cosas.txt","w")
    linea = f.readline()
    mi_diccionario = Diccionario.objects.get(pk=id_diccionario)
    fecha_ultima_jugada = mi_diccionario.fecha_ultima_jugada
    jugada_diccionario = mi_diccionario.jugada
    

    palabra_A = ""
    palabra_B = ""
    mi_palabra = Palabra()


    while linea != "":
        empiezaA = linea.find(".1=")
        empiezaB = linea.find(".2=")
        empiezaDUE = linea.find(".DUE=")
        empiezaLAST = linea.find(".LAST=")
        lista = []
        if empiezaDUE !=-1:
            fecha_desde = linea[(empiezaDUE+5):]
            posfechaOK = fecha_desde.find("=")
            fechaOK = fecha_desde[(posfechaOK+1):]
            lista = fechaOK.split()
            fecha_prox = datetime.strptime(lista[0], "%d/%m/%Y")
            g.write("Due: "+lista[0]+"\n\r")
            print ("Due: "+lista[0])
        if empiezaLAST !=-1:
            fecha_desde = linea[(empiezaLAST+6):]
            posfechaOK = fecha_desde.find("=")
            fechaOK = fecha_desde[(posfechaOK+1):]
            lista = fechaOK.split()
            fecha_Last = datetime.strptime(lista[0], '%d/%m/%Y')
            dias = (fecha_prox - fecha_Last).days
            g.write("LAST: "+str(fecha_Last)+"\n\r")
            g.write("Dias: "+str(dias)+"\n\r")
            print ("LAST: "+str(fecha_Last))
        if empiezaA != -1:
            palabra_A = linea[(empiezaA+3):]
            palabra_Aok = palabra_A[:-2]
            print palabra_Aok
            mi_palabra.palabra_A = palabra_Aok.decode('latin1')
            # mi_palabra.palabra_A = smart_text(palabra_A, encoding='utf-8', strings_only=False, errors='strict')
            g.write(palabra_A)
        if empiezaB != -1:
            palabra_B = linea[(empiezaB+3):]
            palabra_Bok = palabra_B[:-2]
            print palabra_B
            mi_palabra.palabra_B = palabra_Bok.decode('latin1')
            # mi_palabra.palabra_B = smart_text(  palabra_B, encoding='utf-8', strings_only=False, errors='strict') 
            g.write(palabra_B)
            g.write("----------------------\n\r")
            mi_palabra.diccionario = mi_diccionario
            mi_palabra.jugada_proxima = dias+mi_diccionario.jugada
            mi_palabra.save()
            mi_palabra = Palabra()
        linea = f.readline()
    g.close()
    f.close()
    print "Completado!!!!"


def convertir():
    f = open("pruebas.ltm")
    g = open("cosas.txt","w")
    linea = f.readline()
    palabra_A = ""
    palabra_B = ""
    fecha=""
    hoy = datetime.today()


    while linea != "":
        empiezaA = linea.find(".1=")
        empiezaB = linea.find(".2=")
        empiezaDUE = linea.find(".DUE=")
        empiezaLAST = linea.find(".LAST=")
        lista = []
        if empiezaDUE !=-1:
            fecha_desde = linea[(empiezaDUE+5):]
            posfechaOK = fecha_desde.find("=")
            fechaOK = fecha_desde[(posfechaOK+1):]
            lista = fechaOK.split()
            fecha_prox = datetime.strptime(lista[0], '%d/%m/%Y')
            g.write("Due: "+lista[0]+"\n\r")
            print ("Due: "+lista[0])
        if empiezaLAST !=-1:
            fecha_desde = linea[(empiezaLAST+6):]
            posfechaOK = fecha_desde.find("=")
            fechaOK = fecha_desde[(posfechaOK+1):]
            lista = fechaOK.split()
            fecha_Last = datetime.strptime(lista[0], '%d/%m/%Y')
            dias = (fecha_prox - fecha_Last).days
            g.write("LAST: "+str(fecha_Last)+"\n\r")
            g.write("Dias: "+str(dias)+"\n\r")
            print ("LAST: "+str(fecha_Last))
        if empiezaA != -1:
            palabra_A = linea[(empiezaA+3):]
            print palabra_A
            # mi_palabra.palabra_A = palabra_A
            g.write(palabra_A)
        if empiezaB != -1:
            palabra_B = linea[(empiezaB+3):]
            print palabra_B
            # mi_palabra.palabra_B = palabra_B
            g.write(palabra_B)
            g.write("----------------------\n\r")
        linea = f.readline()
    g.close()
    f.close()

def borrar(mi_diccionario):
    diccionario = Diccionario.objects.get(pk = mi_diccionario)
    lista = Palabra.objects.filter(diccionario = diccionario)
    for pal in lista:
        pal.delete()

