
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from wfm.base.models import Depoimento


def home(request):
    return render(request, 'base/index.html', context={'depoimentos': Depoimento.objects.select_related('usuario')})


def sobre(request):
    return render(
        request, 'base/sobre.html',
    )


def servicos(request):
    return render(
        request, 'base/servicos.html',
    )


def depoimentos(request):
    return render(
        request, 'base/depoimentos.html',
        context={'depoimentos': Depoimento.objects.select_related('usuario')}
    )


def loja(request):
    return render(
        request, 'base/loja.html',
    )


def apoiadores(request):
    return render(
        request, 'base/apoiadores.html',
    )


def galeria(request):
    return render(
        request, 'base/galeria.html',
    )


def contato(request):
    return render(
        request, 'base/contato.html',
    )


def inscricao(request, slug):
    return render(
        request, 'base/inscricao.html', context={'slug': slug.replace('-', ' ').title()},
    )

