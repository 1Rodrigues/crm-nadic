from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.db.models import Sum
from django.urls import reverse_lazy
from .models import Produto, Venda, ItemVenda
from .forms import ItemVendaForm
# Create your views here.

class ProdutoList(ListView):
    model = Produto
    template_name = 'produtos_lista.html'

class ProdutoCreate(CreateView):
    model = Produto
    fields = ['nome','preco', 'estoque']
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produto-list')

class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['nome','preco', 'estoque']
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produto-list')

class ProdutoDelete(DeleteView):
    model  = Produto
    template_name = 'produto_confirm_delete.html'
    success_url = reverse_lazy('produto-list')

def dashboard_crm(request):
    faturamento = Venda.objects.filter(status= 'CONCLUIDA').aggregate(Sum('total'))['total__sum']
    if faturamento is None:
        faturamento = 0
    contexto = {
        'faturamento_total': faturamento,
        'vendas_realizadas': Venda.objects.filter(status = 'CONCLUIDA').count(),
    }
    return render(request,'dashboard.html', contexto)

def CriarVenda(request):
    venda = Venda.objects.create()
    return redirect()

