from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'gestoreventos/index.html')

def teste(request):
    return render(request, 'gestoreventos/teste.html')
