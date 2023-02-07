from django import forms
from aplicacion1.models import Creacion

class formproduct(forms.Form):
    name = forms.CharField(max_length=100, label="Nombre")
    price = forms.FloatField(label="Precio")
    stock = forms.BooleanField(required=False)
    product_picture = forms.ImageField(required=False, label="Imagen del Prodcuto")

class UpdateProduct(forms.ModelForm):
    class Meta: 
        model = Creacion
        fields = ["name", "price", "stock", "product_picture"]
        labels = {"name":"Nombre", "price":"Precio" ,"stock":"Stock", "product_picture" : "Imagen de Perfil"}