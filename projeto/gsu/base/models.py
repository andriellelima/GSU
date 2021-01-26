from django.db import models
from django.contrib.auth.models import User
from gsu.setor.models import Setor, Servico
# from base.choice import CAMPUS_CHOICES


class Usuario(User):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField('CPF', max_length=15, null=False, blank=False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuários'
        
    def __str__(self):
        return self.username

class Sugestao(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    email = models.CharField(verbose_name='E-mail para contato', max_length=50, null=True, blank=True)
    descricao = models.TextField('Descrição')

    class Meta:
        verbose_name = 'Sugestão'
        verbose_name_plural = 'Sugestões'
        ordering = ['titulo']
        
    def __str__(self):
        return self.titulo
