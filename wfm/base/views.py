from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.urls import reverse

from wfm.base.models import Depoimento, User, Foto


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
        context={'fotos': Foto.objects.select_related('evento')}
    )


def contato(request):
    return render(
        request, 'base/contato.html',
    )


def inscricao(request, slug):

    if request.method == 'POST':
        try:
            params = request.POST.dict()
            params['picture'] = request.FILES.dict()['picture']
            del params['csrfmiddlewaretoken']
            new_user = User.objects.create_user(**params)
            new_user.is_superuser = False
            new_user.is_staff = False
            new_user.save()
        except Exception as e:
            messages.error(request, f'Erro ao salvar informações!\n{e}')
        else:
            messages.info(request, 'Suas informações foram salvas com sucesso! Um de nossos colaboradores entrará em contato.')

        return redirect(reverse('base:home'))
    else:
        return render(
            request, 'base/inscricao.html', context={'slug': slug.replace('-', ' ').title()},
    )

