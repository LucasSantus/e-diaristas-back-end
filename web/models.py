from django.db import models

class Diarista(models.Model):
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=11)
    logradouro = models.CharField(max_length=60)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=30)
    complemento = models.CharField(max_length=100, null=False, blank=True)
    cep = models.CharField(max_length=8)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=30, null=False, blank=True)
    codigo_ibge = models.IntegerField()
    foto_usuario = models.ImageField(null=False)