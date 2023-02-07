from django import forms
from aplicacion1.models import Creacion

class formproduct(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.FloatField()
    stock = forms.BooleanField(required=False)
    image = forms.ImageField(required=False)