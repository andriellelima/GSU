# Generated by Django 2.2.6 on 2019-11-18 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0004_auto_20191118_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='tipo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de serviço'),
        ),
    ]