from pickletools import read_bytes1

from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=30)
    preco  = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.nome}: R$ {self.preco}'

class Venda(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f'Venda:{self.id}, Valor: {self.total}'

class ItemVenda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE,related_name='itens')
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        if self.produto.estoque >= self.quantidade:
            self.produto.estoque -= self.quantidade
            self.produto.save()
        else:
            raise Exception('Estoque insuficiente')
        self.venda.total += self.preco_unitario * self.quantidade
        self.venda.save()
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.produto.nome} x {self.quantidade} = {self.preco_unitario * self.quantidade}'



