from django.urls import path
from . import views

app_name = 'gestoreventos'

urlpatterns = [
    #pagina inicial
    path('', views.index, name='index'),
    path('teste', views.teste, name='teste'),
    
]