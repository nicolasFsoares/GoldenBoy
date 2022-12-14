from django.shortcuts import render, redirect
from busca.models import Jogador, Busca, Clube, Posicao, Categoria, Conexao
from busca.forms import JogadorForm, ConexaoForm

# Create your views here.

def form(request):
    data = {}
    data['form'] = Jogador()
    return render(request, 'jogadorEdit.html', data)

def home(request):
    dadosBusca = {}
    dadosBusca['dados'] = Busca.objects.select_related('categoria', 'clube', 'posicao')
    return render(request, 'buscaNew.html', dadosBusca)


def jogador(request, pk):
    data = {}
    data['db'] = Jogador.objects.get(pk=pk)
    return render(request, 'jogador.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Jogador.objects.get(pk=pk)
    data['form'] = JogadorForm(instance=data['db'])
    return render(request, 'jogadorEdit.html', data)

def update(request, pk):
    data = {}
    data['db'] = Jogador.objects.get(pk=pk)
    form = JogadorForm(request.POST or None, request.FILES, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Conexao.objects.get(pk=pk)
    db.delete()
    return redirect('home')


# =======================================
# Parte da conexao entre jogador e clube

def conexao(request, pk):
    data = {}
    data['dados'] = Busca.objects.select_related('categoria', 'clube', 'posicao').get(pk=pk)
    return render(request, 'conexao.html', data)

def formConexao(request):
    data = {}
    data['form'] = ConexaoForm()
    return render(request, 'conexao.html', data)

def createConexao(request):
    form = ConexaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def conexoes(request, pk):
    data = {}
    data['dados'] = Conexao.objects.select_related('jogador', 'clube').filter(jogador=pk)
    return render(request, 'conexoes.html', data)