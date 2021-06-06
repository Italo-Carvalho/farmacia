from django.shortcuts import render, redirect, get_object_or_404
from .forms import FuncionarioForm, ProdutoForm
from .models import Produto, Funcionario, Ordem_de_Compra
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from  django.contrib.auth.models import User
from django.db.models import Sum
from django.http import JsonResponse

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('loja')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='/loja')
def home(request):
    if request.method == 'POST':
        formfuncionario = FuncionarioForm(request.POST)
        formproduto = ProdutoForm(request.POST, request.FILES)

        if formfuncionario.is_valid():
            formfuncionario.save()       

        if formproduto.is_valid():
            formproduto.save()   

        return redirect('home')

    else:

        formfuncionario = FuncionarioForm()
        formproduto = ProdutoForm()
        funcionario = Funcionario.objects.all()
        produto = Produto.objects.all()
        ordens = Ordem_de_Compra.objects.all()


    context = {
        'formfuncionario':formfuncionario,
        'formproduto':formproduto,
        'funcionario':funcionario,
        'produto':produto,
        'ordens':ordens,
    }
    return render(request, 'home.html', context)

def loja(request):
    produtos = Produto.objects.all()
    context = {
        'produtos':produtos
    }
    return render(request, 'loja.html', context)

def deletar_objeto(obj, pk):
    obj = get_object_or_404(obj, pk=pk)
    obj.delete()

def deletar_funcionario(request, pk):
    deletar_objeto(Funcionario, pk)
    return redirect('home')

def deletar_produto(request, pk):
    deletar_objeto(Produto, pk)
    return redirect('home')

def deletar_ordem_em_fila(request):
    ordem = Ordem_de_Compra.objects.all().order_by('pk')
    for x in ordem:
        x.delete()
        return redirect('home')


def compra_produto(request, produto_pk, user_pk):
    produto = get_object_or_404(Produto, pk=produto_pk)
    comprador = get_object_or_404(User, pk=user_pk)

    if produto.estoque != 0:
        produto.estoque = produto.estoque - 1
        ordem = Ordem_de_Compra(comprador=comprador, produto=produto)
        ordem.save()
        produto.save() 
        messages.add_message(request, messages.INFO, 'Compra realizada com sucesso! ')
        messages.add_message(request, messages.INFO, f'Comprador: {ordem.comprador.username}')
        messages.add_message(request, messages.INFO, f'Produto: {ordem.produto.nome}')
        messages.add_message(request, messages.INFO, f'Preço: R$ {ordem.produto.preco}')
    return redirect('loja')



def particao(vetor, inicio, final):
  pivo = vetor[final]
#   time.sleep(1.0)
  i = inicio - 1

  for j in range(inicio, final):
    if vetor[j] <= pivo:
      i += 1
      vetor[i], vetor[j] = vetor[j], vetor[i]
  vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]
  return i + 1

def quick_sort(vetor, inicio, final):
  if inicio < final:
    posicao = particao(vetor, inicio, final)
    # Esquerda
    quick_sort(vetor, inicio, posicao - 1)
    # Direito
    quick_sort(vetor, posicao + 1, final)
  return vetor


def compras_quicksort_chart(request):
    labels = []
    data = []

    queryset = Produto.objects.all()
    for entry in queryset:
        labels.append('')
        data.append(int(entry.compras.count() * entry.preco))
        
    
    return JsonResponse(data={
        'labels': labels,
        'data': quick_sort(data, 0, len(data) - 1),
    })


def compras_chart(request):
    labels = []
    data = []

    queryset = Produto.objects.all()
    for entry in queryset:
        labels.append(entry.nome)
        data.append(int(entry.compras.count() * entry.preco))
        
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })




