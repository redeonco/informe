from django.db import models
from datetime import datetime


class Departamentos(models.Model):
    departamento = models.CharField(max_length=100, verbose_name='Departamento')

    def __str__(self):
        return self.departamento

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'


class Filial(models.Model):
    filial = models.CharField(max_length=150, verbose_name='Nome da Filial')

    def __str__(self):
        return self.filial

    class Meta:
        verbose_name = 'Filial'
        verbose_name_plural = 'Filiais'


class FormularioPadrao(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Formulário')
    descricao = models.CharField(max_length=250, verbose_name='Descrição do Formulário')
    departamento = models.ForeignKey(Departamentos, verbose_name='Departamento', on_delete=models.PROTECT)
    data_publicacao = models.DateTimeField(default=datetime.now, verbose_name='Data de Publicação')
    arquivo = models.FileField(upload_to='formularios', verbose_name='Arquivo')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Formulário Padrão'
        verbose_name_plural = 'Formulários Padrão'


class POP(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do POP')
    descricao = models.CharField(max_length=250, verbose_name='Descrição do POP')
    departamento = models.ForeignKey(Departamentos, verbose_name='Departamento', on_delete=models.PROTECT)
    data_publicacao = models.DateTimeField(default=datetime.now, verbose_name='Data de Publicação')
    arquivo = models.FileField(upload_to='pop', verbose_name='Arquivo')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Procedimento Operacional Padrão'
        verbose_name_plural = 'Procedimentos Operacionais Padrão'


class Alvaras(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Documento')
    descricao = models.CharField(max_length=250, verbose_name='Descrição do Documento')
    filial = models.ForeignKey(Filial, verbose_name='Filial', on_delete=models.PROTECT)
    data_vigencia = models.DateField(verbose_name='Data de Vigência')
    data_publicacao = models.DateTimeField(default=datetime.now, verbose_name='Data de Publicação')
    arquivo = models.FileField(upload_to='alvaras_licencas', verbose_name='Arquivo')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Alvarás e Licenças de Funcionamento'
        verbose_name_plural = 'Alvarás e Licenças de Funcionamento'

