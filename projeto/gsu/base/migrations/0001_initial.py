# Generated by Django 2.2.6 on 2019-11-17 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('setor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('matricula', models.CharField(max_length=15, verbose_name='Matrícula')),
                ('funcao', models.CharField(max_length=50, verbose_name='Função')),
                ('setor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setor.Setor')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuários',
            },
        ),
    ]
