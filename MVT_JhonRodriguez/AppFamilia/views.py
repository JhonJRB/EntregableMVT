from django import http
from django.http import HttpResponse
from django.shortcuts import render
from AppFamilia.models import FamiliaBD
from django.template import loader

# Create your views here.
def cargarFamilia(request,nombre,edad,fecha):
    familiar1=FamiliaBD(nombre=nombre,edad=edad,fecha=fecha)
    familiar1.save()
    texto=f"Se guardo en base de datos {nombre} {edad} {fecha}"
    return HttpResponse(texto)

def datosFamilia(request):
      
    familiares=FamiliaBD.objects.all()
    flia={"familiares":familiares}
    plantillas=loader.get_template('template.html') 
    documento=plantillas.render(flia)  
    return HttpResponse(documento)
    
