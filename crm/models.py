from pickletools import read_bytes1
from django.db.models import F
from django.db import transaction
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
    status = models.CharField(max_length=20, choices=[('PENDENTE', 'pendente'),('CONCLUIDA','concluida')], default = 'PENDENTE')

    def concluir(self):
        if self.status != 'PENDENTE':
            return
        with transaction.atomic():
            soma_total = 0
            for item in self.itens.select_related('produto'):
                if item.produto.estoque < item.quantidade:
                    raise Exception('Estoque insuficiente')
                Produto.objects.filter(id=item.produto.id).update(
                    estoque=F('estoque') - item.quantidade
                )
            self.total = soma_total
            self.status = 'CONCLUIDA'
            self.save()
    def calcular_valor(self):
        total = 0
        for item in self.itens.all():
            total += item.preco_unitario * item.quantidade
        return total
    def __str__(self):
        return f'Venda:{self.id}, Valor: {self.total}'

class ItemVenda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE,related_name='itens')
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.produto.nome} x {self.quantidade} = {self.preco_unitario * self.quantidade}'



