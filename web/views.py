from django.shortcuts import render, redirect
from .forms import DiaristaForm
from .models import Diarista
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'index.html')

def cadastrar_diarista(request):
    if request.method == 'POST':
        form = DiaristaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_diaristas')

    else:
        form = DiaristaForm()

    context = {
        'form': form,
    }

    return render(request, 'web/cadastrar_diarista.html', context)

def listar_diaristas(request):
    diaristas = Diarista.objects.all()

    context = {
        'diaristas': diaristas,
    }

    return render(request, 'web/listar_diaristas.html', context)

def alterar_diarista(request, id_diarista):
    diarista = Diarista.objects.get(id=id_diarista)
    if request.method == "POST":
        form = DiaristaForm(request.POST or None, request.FILES, instance=diarista)
        if form.is_valid():
            form.save()
            return redirect('listar_diaristas')
    else:
        form = DiaristaForm(instance=diarista)
        
    context = {
        'form': form,
    }

    return render(request, 'web/cadastrar_diarista.html', context)

def remover_diarista(request, id_diarista):
    diarista = Diarista.objects.get(id=id_diarista)
    diarista.delete()

    return redirect('listar_diaristas')