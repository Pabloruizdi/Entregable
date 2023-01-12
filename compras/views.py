from django.shortcuts import render
from django.http import HttpResponse

from compras.models import Ordenes
from compras.forms2 import formcompra

#def lista_ordenes(request):
    #ordenes = Ordenes.objects.all()
    #context = {
    #    "ordenes":ordenes,
    #}
    #return render(request, "Compras/compra.html", context=context)


def creacion_orden(request):
    if request.method == "GET":
        context = {
            "Payment": formcompra()
        }

        return render(request, "Compras/compra.html", context = context)

    elif request.method == "POST":
        form = formcompra(request.POST)
        if form.is_valid():
            Ordenes.objects.create(
                cliente = form.cleaned_data["nombre"],
                producto = form.cleaned_data["precio"],
                paymentmethod = form.cleaned_data["metodo de pago"]
            )
            context = {
                "message": "su producto se encuentra en el carrito"
            }
            return render(request,"Compras/compra.html", context=context )
        else: 
            context = {
                "message": "Su producto se encuentra en el carrito"
            }
            context = {
                "form_errors": form.errors,
                "form": formcompra()
            }
            return render(request,"Compras/compra.html", context=context)

