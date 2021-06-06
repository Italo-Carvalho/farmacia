from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Ordem_de_Compra)
class Ordem_de_CompraAdmin(admin.ModelAdmin):
    list_display = ('produto',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome',)