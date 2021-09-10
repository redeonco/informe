from django.urls import path
from .views import home, FormulariosList, POPView, AlvarasView, filtra_formularios

urlpatterns = [
    path('', home, name='home'),
    path('formularios/', FormulariosList.as_view(), name='formularios'),
    path('pop/', POPView.as_view(), name='pop'),
    path('alvaras_licenciamento/', AlvarasView.as_view(), name='alvaras_licenciamento'),
    path('filtra_formularios/', filtra_formularios, name='filtra_formularios'),
]
