from django import forms
from compras.models import Payment

class formcompra(forms.Form):
    cliente = forms.CharField(max_length=100, label="Cliente")
    producto = forms.CharField(max_length=100, label="producto")
    paymentmethod = forms.ModelChoiceField(queryset=Payment.objects.all(), label="Metodo de pago")