from django.db.models import fields
from django.forms import ModelForm
from .models import Produto, Funcionario


class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'sobrenome', 'cargo', 'salario']

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'imagem', 'estoque']