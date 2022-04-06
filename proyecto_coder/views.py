from unittest import loader
from django.http import HttpResponse
from django.template import Template,Context,loader
from datetime import datetime
def primer_vista(request):
    return HttpResponse("Hola Familia ")


def familia(request):
 archivo = open(r'C:\Users\Usuario\Desktop\ProyectoMVT\proyecto_coder\proyecto_coder\templates\page.html')
 nombre="dario"
 edad=29
 fecha_nacimiento="1992-25-05"
 
 dict_context={"nombre": nombre,"edad":edad,"fecha_nacimiento":fecha_nacimiento,"nombre2":"juan","edad2":20,"fecha_nacimiento_2":"2000-05-25","nombre3":"Luis","edad3":20,"fecha_nacimiento_3":"2000-05-25"}
 
 plantilla = loader.get_template("page.html")


 documento= plantilla.render(dict_context)
 return HttpResponse(documento)