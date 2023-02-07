from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from ventas.models import Ordeness
from ventas.forms2 import formcompra




# def creacion_orden(request):
#     if request.method == "GET":
#         context = {
#             "Payment": formcompra()
#         }

#         return render(request, "Compras/compra.html", context = context)

#     elif request.method == "POST":
#         form = formcompra(request.POST)
#         if form.is_valid():
#             Ordeness.objects.create(
#                 cliente = form.cleaned_data["cliente"],
#                 producto = form.cleaned_data["producto"],
#                 paymentmethod = form.cleaned_data["paymentmethod"],
#             )
#             context = {
#                 "message": "su producto se encuentra en el carrito"
#             }
#             return render(request,"Compras/compra.html", context=context )
#         else: 
#             context = {
#                 "message": "Su producto se encuentra en el carrito"
#             }
#             context = {
#                 "form_errors": form.errors,
#                 "form": formcompra()
#             }
#             return render(request,"Compras/compra.html", context=context)


def creacion_orden(request):
    if request.method == "GET":
        form = formcompra(request.POST)
        if form.is_valid():
            Ordeness.objects.create(
                cliente = form.cleaned_data["cliente"],
                producto = form.cleaned_data["producto"],
                paymentmethod = form.cleaned_data["paymentmethod"],
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
    elif request.method == "POST":
        form = formcompra(request.POST)
        if form.is_valid():
            Ordeness.objects.create(
                cliente = form.cleaned_data["cliente"],
                producto = form.cleaned_data["producto"],
                paymentmethod = form.cleaned_data["paymentmethod"],
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


