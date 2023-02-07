from django import forms
from ventas.models import Pagoo

class formcompra(forms.Form):
    cliente = forms.CharField(max_length=100, label="Cliente")
    producto = forms.CharField(max_length=100, label="producto")
    paymentmethod = forms.ModelChoiceField(queryset=Pagoo.objects.all(), label="Metodo de pago")

