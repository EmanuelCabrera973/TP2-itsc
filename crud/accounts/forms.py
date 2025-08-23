from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()
    
    class Meta:
        user = User
        fields = ("usuario", "email", "contraseña1", "contraseña2", "captcha")
        