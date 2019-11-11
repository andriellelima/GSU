from django.db import models
from django.contrib.auth.models import User
# from base.choice import CAMPUS_CHOICES

class Setor(models.Model):
    nome = models.CharField("Nome do Setor",max_length=100)
    reponsavel = models.CharField("Nome do Resposávek",max_length=100)
    bloco = models.CharField('Bloco', max_length=50)
    andar = models.CharField('Andar',max_length=30)
    sala = models.CharField('Sala',max_length=50)
    horario = models.CharField("horário de atendimento",max_length=30)
    telefone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Servico(models.Model):
    titulo = models.CharField(max_length=100)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    descricao = models.TextField('Descrição', blank=False)
    documentos = models.CharField('Documentos', max_length=250)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo    


class Usuario(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, editable=True,  related_name='usuario_set', on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, null=True, blank=True,on_delete=models.CASCADE)
    cpf = models.CharField('CPF', max_length=11)
    matricula = models.CharField('Matrícula', max_length=15)
    funcao = models.CharField('Função', max_length=50)
    # nome = models.CharField(max_length=100)
    # campus = models.CharField(max_length=100,choices=CAMPUS_CHOICES)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuários'
        
    def __str__(self):
        return self.user.name