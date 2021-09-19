from django.urls import path
from .views import (
    home,
    FormulariosList,
    POPView,
    AlvarasView,
    filtra_formularios,
    filtra_pop,
    filtra_filial,
    suporte,
    UtilitariosView,
    SearchView,
)

urlpatterns = [
    path('', home, name='home'),
    path('formularios/', FormulariosList.as_view(), name='formularios'),
    path('pop/', POPView.as_view(), name='pop'),
    path('alvaras_licenciamento/', AlvarasView.as_view(), name='alvaras_licenciamento'),
    path('suporte/', suporte, name='suporte'),
    path('suporte/utilitarios/', UtilitariosView.as_view(), name='utilitarios'),
    path('search/', SearchView.as_view(), name='search'),
    path('filtra_formularios/', filtra_formularios, name='filtra_formularios'),
    path('filtra_pop/', filtra_pop, name='filtra_pop'),
    path('filtra_filial/', filtra_filial, name='filtra_filial'),
]
