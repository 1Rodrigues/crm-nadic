from django import forms
from .models import ItemVenda

class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVenda
        fiels = ['produto', 'quantidade']
