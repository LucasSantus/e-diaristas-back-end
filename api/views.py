from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

class DiaristasCidadeList(APIView):
    def get(self, request, format=None):
        cep = self.request.query_params.get('cep', None)
