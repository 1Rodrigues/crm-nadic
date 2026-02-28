from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
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

def criar_venda(request):
    venda = Venda.objects.create()
    return redirect('detalhe_venda', pk=venda.pk)

def detalhe_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        form = ItemVendaForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.venda = venda
            item.preco_unitario = item.produto.preco
            item.save()
            return redirect('detalhe_venda',pk)
    else:
        form = ItemVendaForm()
    context = {
        'venda': venda,
        'itens': venda.itens.all(),
        'form': form,
    }
    return render(request,'detalhe_venda.html', context)

def concluir_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    try:
        venda.concluir()
        return redirect('dashboard')
    except Exception as e :
        return render(request, 'erro.html', {'mensagem': str(e)})

def remover_item(request, pk):
    item = get_object_or_404(pk)
    ItemVenda.objects.delete(id=pk)
    

