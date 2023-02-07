from django.shortcuts import render
from django.http import HttpResponse

from aplicacion1.models import Creacion
from aplicacion1.forms import formproduct




def creacion_producto(request):
    if request.method == "GET":
        context = {
            "form": formproduct()
        }
    
        return render (request, "productos/creacionproductos.html", context=context)

    elif request.method == "POST": 
        form = formproduct(request.POST)
        if form.is_valid():
            Creacion.objects.create(
                name = form.cleaned_data["name"],
                price = form.cleaned_data["price"],          
                stock = form.cleaned_data["stock"],
                image = form.cleaned_data["image"],
            )
            context = {
                "message": "Producto creado exitosamente"
            }
            return render(request,"productos/creacionproductos.html", context=context )
        else:
            context = {
                "message": "Producto creado exitosamente"
            }
            context = {
                "form_errors": form.errors,
                "form": formproduct()
            }
            return render(request,"productos/creacionproductos.html", context=context)





def lista_productos(request):
    if "search" in request.GET:
        search = request.GET["search"]
        all_productos = Creacion.objects.filter(name__contains = search)
    else: 
        all_productos = Creacion.objects.all()
    context = {
        "productos":all_productos,
    }

    return render(request,"productos/listaproductos.html", context=context)


