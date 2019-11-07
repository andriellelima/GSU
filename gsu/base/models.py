from django.db import models
from django.contrib.auth.models import User
from base.choice import CAMPUS_CHOICES

class Setor(models.Model):
    nome = models.CharField("Nome do Setor",max_length=100)
    reponsavel = models.CharField("Nome do Resposávek",max_length=100)
    descricao = models.CharField("Descrição do(s) serviço(s)",max_length=1000)
    documento = models.CharField("Documentos necessários",max_length=200)
    bloco = models.CharField(max_length=50)
    andar = models.CharField(max_length=30)
    sala = models.CharField(max_length=50)
    horario = models.CharField("horário de atendimento",max_length=30)
    telefone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, editable=True,  related_name='usuario_set', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    campus = models.CharField(max_length=100,choices=CAMPUS_CHOICES)
    setor = models.ForeignKey(Setor, null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome