from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def creacion_orden(request):
    return render(request, "Compras/compra.html", context={})
