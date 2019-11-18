from django.db import models

# Create your models here.
class Setor(models.Model):
    nome = models.CharField('Nome do Setor',max_length=100)
    descricao = models.TextField('Descrição',blank=True)
    reponsavel = models.CharField('Nome do Resposávek',max_length=100)
    bloco = models.CharField('Bloco', max_length=50)
    andar = models.CharField('Andar',max_length=30)
    sala = models.CharField('Sala',max_length=50)
    horario = models.CharField('horário de atendimento',max_length=30) #DataTimeField
    telefone = models.CharField('Telefone',max_length=10) 
    email = models.CharField('E-mail',max_length=100)

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Diretoria(models.Model):
    nome = models.CharField('Titulo da diretoria', max_length=50)
    responsavel = models.CharField('Responsavel', max_length=50)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    telefone = models.CharField('Telefone', max_length=15)

    class Meta:
        verbose_name = 'Diretoria'
        verbose_name_plural = 'Diretorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Servico(models.Model):
    titulo = models.CharField('Titulo',max_length=100)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    tipo = models.CharField('Tipo de serviço', max_length=50, null=True, blank=True)
    descricao = models.TextField('Descrição', blank=False)
    documentos = models.CharField('Documentos', max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
