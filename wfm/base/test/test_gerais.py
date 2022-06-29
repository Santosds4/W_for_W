import pytest
from django.urls import reverse
from django.test import Client


@pytest.fixture
def cl(client: Client, db):
    return client

@pytest.mark.parametrize(
    'pagina',
    [
        ('base:home', ''),
        ('base:sobre', ''),
        ('base:servicos', ''),
        ('base:depoimentos', ''),
        ('base:loja', ''),
        ('base:apoiadores', ''),
        ('base:galeria', ''),
        ('base:contato', ''),
        ('base:inscricao', 'receba-apoio'),
        ('base:inscricao', 'apoie'),
    ]
)
def test_status_code(pagina, cl):
    print(f'{pagina= }')
    if pagina[1]:
        resp = cl.get(reverse(pagina[0], kwargs={'slug': f'{pagina[1]}'}))
    else:
        resp = cl.get(reverse(pagina[0]))
    assert resp.status_code == 200
