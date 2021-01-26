from django.db import models
from django.contrib.auth.models import User
# from projeto.gsu.base.models import Usuario

# Create your models here.
class Setor(models.Model):
    nome = models.CharField('Nome do Setor',max_length=100)
    descricao = models.TextField('Descrição',blank=True)
    responsavel = models.CharField('Nome do Resposável',max_length=100)
    localizacao = models.CharField('Localizacao(Link do Mapa da UFAC)', max_length=500)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    telefone = models.CharField('Telefone',max_length=20) 
    email = models.CharField('E-mail',max_length=100)
    user = models.ForeignKey(User, null=True, default=None, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Servico(models.Model):
    titulo = models.CharField('Titulo',max_length=100)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    descricao = models.TextField('Descrição', blank=False)
    documentos = models.CharField('Documentos', max_length=250, null=True, blank=True)
    informacoes = models.CharField('Mais informações(site UFAC)', max_length=250, null=True, blank=True)


    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
