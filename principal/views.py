from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso


def main(request):
    cursos = Curso.objects.all()
    return render(request, 'principal/index.html', {"cursos":cursos})

