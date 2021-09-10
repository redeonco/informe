from django.shortcuts import render
from django.views.generic import ListView
from .models import FormularioPadrao, POP, Alvaras, Departamentos

from django.core import serializers
from django.http import HttpResponse


def home(request):
    return render(request, 'core/index.html')


class FormulariosList(ListView):
    model = FormularioPadrao


class POPView(ListView):
    model = POP


class AlvarasView(ListView):
    model = Alvaras


def filtra_formularios(request):
    depart = request.GET['outro_param']
    departamento = Departamentos.objects.get(id=depart)

    qs_json = serializers.serialize('json', departamento.formulariopadrao_set.all())
    return HttpResponse(qs_json, content_type='application/json')
