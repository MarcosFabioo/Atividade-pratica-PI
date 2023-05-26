from django.contrib import admin
from .models import Categoria, Cliente, Locacao, Filme


# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome_categoria",)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome_cliente", "email")


@admin.register(Locacao)
class LocacaoAdmin(admin.ModelAdmin):
    list_display = ("nome_locacao", "data", "cliente")


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ("titulo_filme", "valor", "categoria")
