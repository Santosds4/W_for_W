from django.urls import path

from wfm.base.views import home, depoimentos, sobre, loja, servicos, apoiadores, contato, galeria, inscricao

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('sobre/', sobre, name='sobre'),
    path('servicos/', servicos, name='servicos'),
    path('depoimentos/', depoimentos, name='depoimentos'),
    path('loja/', loja, name='loja'),
    path('apoiadores/', apoiadores, name='apoiadores'),
    path('galeria/', galeria, name='galeria'),
    path('contato/', contato, name='contato'),
    path('inscricao/<slug:slug>', inscricao, name='inscricao'),
]
