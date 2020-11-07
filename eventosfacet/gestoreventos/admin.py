from django.contrib import admin

#import dos modelos 
from gestoreventos.models import Curso, Funcionario, Palestrante, Evento

# Register your models here.
admin.site.register(Curso)
admin.site.register(Funcionario)
admin.site.register(Evento)
admin.site.register(Palestrante)