from django.shortcuts import render

def Index(request):
    return render(request, "Inicio/Index.html", context= {})

def Nosotros(request):
    return render(request, "Nosotros/sobrenosotros.html", context={})

def Vende(request):
    return render(request, "productos/vendetuP.html", context={})
