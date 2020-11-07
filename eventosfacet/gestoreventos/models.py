from django.db import models

# Create your models here.


class Curso(models.Model):
    nome_curso = models.CharField(max_length=100)
    codigo_curso = models.IntegerField()

    def __str__(self):
        return self.nome_curso

class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=100)
    matricula = models.IntegerField()
    email = models.CharField(max_length=150)
    curso_vinculado = models.ForeignKey(Curso, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome_funcionario

class Palestrante(models.Model):
    nome_palestrante = models.CharField(max_length=150)
    data_nascimento = models.DateField(auto_now=False, auto_now_add=False)
    cpf = models.CharField(max_length=11)
    email_palestrante = models.CharField(max_length=150)
    telefone = models.CharField(max_length=9)

    def __str__(self):
        return self.nome_palestrante


class Evento(models.Model):
    nome_evento = models.CharField(max_length=200)
    data_inicio = models.DateField(auto_now=False, auto_now_add=False)
    data_fim = models.DateField(auto_now=False, auto_now_add=False)
    curso_organizador = models.ForeignKey(Curso, on_delete=models.RESTRICT, default=1)
    palestrantes = models.ForeignKey(Palestrante, on_delete=models.RESTRICT, default=2)
    organizador = models.ForeignKey(Funcionario, on_delete=models.RESTRICT, default=3)
    descricao = models.CharField(max_length=300, default="teste")
    local = models.CharField(max_length=100, default="Auditorio")

    def __str__(self):
        return self.nome_evento



