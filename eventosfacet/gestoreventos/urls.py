from django.urls import path
from . import views

app_name = 'gestoreventos'

urlpatterns = [
    #pagina inicial
    path('', views.index, name='index'),
    path('cursos', views.cursos, name='cursos'),
    path('eventos', views.eventos, name='eventos'),
    path('novo_curso', views.novo_curso, name='novo_curso'),
    
]