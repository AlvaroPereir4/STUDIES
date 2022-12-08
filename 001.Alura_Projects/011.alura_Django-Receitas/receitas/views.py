from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita


def index(request):
    # informar o nome das receitas, pra linkar o nome no 'index.html'. para o link levar ate a pagina requisitada.
    receitas = Receita.objects.all()
    dados = {
        'receitas':  receitas
    }
    return render(request, 'index.html', dados) 

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : receita
    }

    return render(request, 'receita.html', receita_a_exibir)

