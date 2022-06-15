from django.shortcuts import render
from django.http import HttpResponse
from AppCoder import Curso 
# Create your views here.

def curso(self):
    curso = Curso( nombre ="Web", camada="12345")
    curso.save()

    documentoDeTexto = f"el curso {curso.nombre}, la camda es {curso.camada}" 
