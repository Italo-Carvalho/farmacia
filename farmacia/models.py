from django.db import models
from  django.contrib.auth.models import User



class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=20, decimal_places=2)
    imagem = models.ImageField('Imagem', upload_to='produtos/')
    estoque = models.IntegerField('Em estoque')
    criado_em = models.DateTimeField('Criado em' ,auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=180)
    cargo = models.CharField('Cargo', max_length=100)
    salario = models.DecimalField('Salario', max_digits=20, decimal_places=2)
    criado_em = models.DateTimeField('Criado em' ,auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.nome

class Ordem_de_Compra(models.Model):
    comprador = models.ForeignKey(User, related_name='compras' , on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='compras', on_delete=models.CASCADE)
    criado_em = models.DateTimeField('Criado em' ,auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.produto.nome