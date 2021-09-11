from django.contrib import admin
from .models import (
    Departamentos,
    FormularioPadrao,
    POP,
    Filial,
    Alvaras,
    Utilitarios
)

admin.site.register(Filial)
admin.site.register(Departamentos)
admin.site.register(FormularioPadrao)
admin.site.register(POP)
admin.site.register(Alvaras)
admin.site.register(Utilitarios)
