from django.shortcuts import render
from .forms import DiaristaForm
from .models import Diarista

def home(request):
    return render(request, 'index.html')

def cadastrar_diarista(request):
    if request.method == 'POST':
        form_diarista = DiaristaForm(request.POST, request.FILES)
        if form_diarista.is_valid():
            form_diarista.save()

    else:
        form_diarista = DiaristaForm()

    context = {
        'form': form_diarista,
    }
    return render(request, 'web/cadastrar_diarista.html', context)

def listar_diaristas(request):
    diaristas = Diarista.objects.all()
    context = {
        'diaristas': diaristas,
    }
    return render(request, 'web/listar_diaristas.html', context)
