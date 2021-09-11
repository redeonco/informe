from django.shortcuts import render
from django.views.generic import ListView
from .models import FormularioPadrao, POP, Alvaras, Departamentos, Filial, Utilitarios

from django.core import serializers
from django.http import HttpResponse


def home(request):
    return render(request, 'core/index.html')


class FormulariosList(ListView):
    model = FormularioPadrao

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departamentos'] = Departamentos.objects.all().order_by('departamento')
        return context


class POPView(ListView):
    model = POP

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departamentos'] = Departamentos.objects.all().order_by('departamento')
        return context


class AlvarasView(ListView):
    model = Alvaras

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filial'] = Filial.objects.all().order_by('filial')
        return context


def filtra_formularios(request):
    depart = request.GET['outro_param']
    departamento = Departamentos.objects.get(id=depart)

    qs_json = serializers.serialize('json', departamento.formulariopadrao_set.all())
    return HttpResponse(qs_json, content_type='application/json')


def filtra_pop(request):
    depart = request.GET['outro_param']
    departamento = Departamentos.objects.get(id=depart)

    qs_json = serializers.serialize('json', departamento.pop_set.all())
    return HttpResponse(qs_json, content_type='application/json')


def filtra_filial(request):
    filial_id = request.GET['outro_param']
    filial = Filial.objects.get(id=filial_id)

    qs_json = serializers.serialize('json', filial.alvaras_set.all())
    return HttpResponse(qs_json, content_type='application/json')


def suporte(request):
    return render(request, 'core/suporte.html')


class UtilitariosView(ListView):
    model = Utilitarios
