from django.db import models

# Create your models here.
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
