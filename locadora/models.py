from django.db import models


# Create your models here.
class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=150)

    def __str__(self):
        return self.nome_categoria


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nome_cliente


class Locacao(models.Model):
    nome_locacao = models.CharField(max_length=200)
    data = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_locacao


class Filme(models.Model):
    titulo_filme = models.CharField(max_length=200)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    locacao = models.ManyToManyField(Locacao)

    def __str__(self):
        return self.titulo_filme
