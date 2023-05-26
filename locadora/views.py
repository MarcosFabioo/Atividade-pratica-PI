from django.shortcuts import render
from .models import Locacao, Filme


# Create your views here.
def index(request):
    return render(request, "index.html")


def lista_locacao(request):
    locacoes = Locacao.objects.all()
    return render(request, "locacao.html", context={"locacoes": locacoes})


def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, "filmes.html", context={"filmes": filmes})
