from django.contrib import admin
from django.urls import path, include
from .views import cadastrar_diarista

urlpatterns = [
    path('cadastrar-ediarista', cadastrar_diarista, name='cadastrar_diarista'),
]
