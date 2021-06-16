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

def alterar_diarista(request, id_diarista):
    diarista = get_object_or_404(Post, id=id_diarista)
    form = DiaristaForm(request.POST or None, instance=diarista)
    if form.is_valid():
        form.save()
        return redirect('listar-diarista', pk=post.pk)

    context = {
        'form': diarista,
    }

    return render(request, 'web/listar_diaristas.html', context)

def remover_diarista(request):
    diaristas = Diarista.objects.all()
    
    context = {
        'diaristas': diaristas,
    }

    return render(request, 'web/listar_diaristas.html', context)
