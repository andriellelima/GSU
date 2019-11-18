# Generated by Django 2.2.6 on 2019-11-17 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Setor')),
                ('reponsavel', models.CharField(max_length=100, verbose_name='Nome do Resposávek')),
                ('bloco', models.CharField(max_length=50, verbose_name='Bloco')),
                ('andar', models.CharField(max_length=30, verbose_name='Andar')),
                ('sala', models.CharField(max_length=50, verbose_name='Sala')),
                ('horario', models.CharField(max_length=30, verbose_name='horário de atendimento')),
                ('telefone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('documentos', models.CharField(max_length=250, verbose_name='Documentos')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setor.Setor')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
                'ordering': ['titulo'],
            },
        ),
    ]