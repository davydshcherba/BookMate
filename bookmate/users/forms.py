from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "input-field"}),
            "email": forms.EmailInput(attrs={"class": "input-field"}),
            "password1": forms.PasswordInput(attrs={"class": "input-field"}),
            "password2": forms.PasswordInput(attrs={"class": "input-field"}),
        }
        help_texts = {field: "" for field in fields}  
