from django.shortcuts import render
from aplicacion1.models import Creacion
from aplicacion1.forms import formproduct, UpdateProduct
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def creacion_producto(request):
    if request.method == "GET":
        context = {
            "form": formproduct()
        }
    
        return render (request, "productos/creacionproductos.html", context=context)

    elif request.method == "POST": 
        form = formproduct(request.POST, request.FILES)
        if form.is_valid():
            Creacion.objects.create(
                name = form.cleaned_data["name"],
                price = form.cleaned_data["price"],          
                stock = form.cleaned_data["stock"],
                product_picture = form.cleaned_data["product_picture"],
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
        "productos":all_productos
    }

    return render(request,"productos/listaproductos.html", context=context)

@user_passes_test((lambda u: u.is_superuser))
def update_product(request, pk):
    product = Creacion.objects.get(id=pk)
    if request.method == "GET":
        context = {
            "form": UpdateProduct(
                initial={
                    "name":product.name,
                    "price":product.price,
                    "stock":product.stock,
                    "product_picture":product.product_picture
                }
            )
        }
    
        return render (request, "productos/update_product.html", context=context)

    elif request.method == "POST": 
        form = UpdateProduct(request.POST, request.FILES)
        if form.is_valid():
            product.name = form.cleaned_data["name"]
            product.price = form.cleaned_data["price"]        
            product.stock = form.cleaned_data["stock"]
            product.product_picture = form.cleaned_data["product_picture"]
            product.save()
            
            context = {
                "message": "Producto actualizado exitosamente"
            }
        else:
            context = {
                "form_errors": form.errors,
                "form": UpdateProduct()
            }
        return render(request,"productos/update_product.html", context=context)


class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        return self.request.user.is_superuse

class ProductDeleteView(DeleteView, SuperUserRequiredMixin):
    model = Creacion 
    template_name = "productos/delete_product.html"
    success_url ="/Lista-Productos/"
    