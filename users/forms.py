from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from users.models import UserProfile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label='Nombre')
    last_name = forms.CharField(max_length=100, required=True, label='Apellido')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



class Updateform(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, label="Nombre de Usuario")
    first_name = forms.CharField(max_length=100, required=True, label='Nombre')
    last_name = forms.CharField(max_length=100, required=True, label='Apellido')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'birth_date', 'profile_image']
        labels = {"phone":"Numero de telefono", "birth_date":"fecha de cumpleaños", "profile_image":"Imagen de perfil"}
