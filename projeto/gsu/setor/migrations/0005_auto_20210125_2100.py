# Generated by Django 3.1.5 on 2021-01-26 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0004_auto_20210125_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='user',
        ),
        migrations.AlterField(
            model_name='setor',
            name='localizacao',
            field=models.CharField(max_length=500, verbose_name='Localizacao(Link do Mapa da UFAC)'),
        ),
    ]
