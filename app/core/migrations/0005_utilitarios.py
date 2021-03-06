# Generated by Django 3.2.7 on 2021-09-11 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_alvaras_arquivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilitarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Utilitário')),
                ('descricao', models.CharField(max_length=250, verbose_name='Descrição do Utilitário')),
                ('data_publicacao', models.DateTimeField(default=datetime.datetime.now, verbose_name='Data de Publicação')),
                ('arquivo', models.FileField(upload_to='utilitarios', verbose_name='Arquivo')),
            ],
        ),
    ]
