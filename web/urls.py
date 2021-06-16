from django.contrib import admin
from django.urls import path, include
from .views import cadastrar_diarista, listar_diaristas

urlpatterns = [
    path('cadastrar-diarista', cadastrar_diarista, name='cadastrar_diarista'),
    path('listar-diaristas', listar_diaristas, name='listar_diaristas'),
]
