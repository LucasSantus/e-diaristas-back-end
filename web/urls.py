from django.contrib import admin
from django.urls import path, include
from .views import cadastrar_diarista, listar_diaristas, alterar_diarista, remover_diarista

urlpatterns = [
    path('cadastrar-diarista/', cadastrar_diarista, name='cadastrar_diarista'),
    path('listar-diaristas/', listar_diaristas, name='listar_diaristas'),
    path('alterar-diarista/<int:id_diarista>', alterar_diarista, name='alterar_diarista'),
    path('remover-diarista/<int:id_diarista>', remover_diarista, name='remover_diarista'),

]