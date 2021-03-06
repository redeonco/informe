# Generated by Django 3.2.7 on 2021-09-09 14:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filial', models.CharField(max_length=150, verbose_name='Nome da Filial')),
            ],
            options={
                'verbose_name': 'Filial',
                'verbose_name_plural': 'Filiais',
            },
        ),
        migrations.AlterModelOptions(
            name='departamentos',
            options={'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.AlterModelOptions(
            name='formulariopadrao',
            options={'verbose_name': 'Formulário Padrão', 'verbose_name_plural': 'Formulários Padrão'},
        ),
        migrations.AlterModelOptions(
            name='pop',
            options={'verbose_name': 'Procedimento Operacional Padrão', 'verbose_name_plural': 'Procedimentos Operacionais Padrão'},
        ),
        migrations.CreateModel(
            name='Alvaras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Documento')),
                ('descricao', models.CharField(max_length=250, verbose_name='Descrição do Documento')),
                ('data_vigencia', models.DateField(verbose_name='Data de Vigência')),
                ('data_publicacao', models.DateTimeField(default=datetime.datetime.now, verbose_name='Data de Publicação')),
                ('arquivo', models.FileField(upload_to='pop', verbose_name='Arquivo')),
                ('filial', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.filial', verbose_name='Filial')),
            ],
            options={
                'verbose_name': 'Alvarás e Licenças de Funcionamento',
                'verbose_name_plural': 'Alvarás e Licenças de Funcionamento',
            },
        ),
    ]
