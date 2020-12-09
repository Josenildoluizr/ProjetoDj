from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Curso, Evento
from .forms import CursoForm

# Create your views here.

def index(request):
    return render(request, 'gestoreventos/index.html')

def cursos(request):
    cursos = Curso.objects.order_by("id")
    contexto = {'cursos': cursos}
    return render(request, 'gestoreventos/cursos.html', contexto)

def eventos(request):
    eventos = Evento.objects.order_by("id")
    contexto = {'eventos': eventos}
    return render(request, 'gestoreventos/eventos.html',contexto)

def novo_curso(request):
    if request.method != 'POST':
        form = CursoForm
    else:
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gestoreventos:cursos'))
    context = {'form': form}
    return render(request, 'gestoreventos/novo_curso.html',context)
