from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import RegisterForm, Updateform, UserProfileForm
from django.contrib.auth.decorators import login_required
from users.models import UserProfile


def login_user(request):
    if request.method == "GET":
        form = AuthenticationForm()
        context = {
            "form" : form
        }
        return render(request, "users/login.html", context=context)

    elif request.method == "POST":
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password  = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                context= {
                    "message": f"bienvenido {username}!!!"
                }
                return render(request, "Inicio/Index.html", context=context)

        form = AuthenticationForm()
        context ={
            'form':form,
            'errors':'Usuario o contraseña incorrectos!'
        }
        return render(request, "users/login.html", context=context)

def register(request):
    if request.method == "GET":
        form = RegisterForm()
        context = {
            "form":form
        }
        return render(request, "users/Singup.html", context=context)

    elif request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            UserProfile.objects.create(user=user)
            return redirect("login")

        context={
            "errors":form.errors,
            "form":RegisterForm()
        }
        return render(request, "users/singup.html", context=context)

@login_required
def update_user(request): 
    user = request.user
    if request.method == "GET":
        form = Updateform(initial = {
            "username":user.username,
            "first_name":user.first_name,
            "last_name":user.last_name
        })
        context = {
            "form":form
        }
        return render(request, "users/Update.html", context=context)

    elif request.method == "POST":
        form=Updateform(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get("username")
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            return redirect("index")

        context={
            "errors":form.errors,
            "form":RegisterForm()
        }
        return render(request, "users/Update.html", context=context)


def update_profile(request):
    user = request.user
    if request.method == 'GET':
        form = UserProfileForm(initial={
            'phone':request.user.profile.phone,
            'birth_date':request.user.profile.birth_date,
            'profile_image':request.user.profile.profile_image
        })
        context ={
            'form':form
        }
        return render(request, 'users/updateprofile.html', context=context)

    elif request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.profile_image = form.cleaned_data.get('profile_image')
            user.profile.save()
            return redirect('index')
        
        context = {
            'errors':form.errors,
            'form':UserProfileForm()
        }
        return render(request, 'users/singup.html', context=context)