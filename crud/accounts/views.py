from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, Login, Logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django,contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(lista_persona)
        else:
            form = CustomUserCreationForm()
        return render(request, 'accounts/register.html',{'form': form})
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usuario')
            password = form.cleaned_data.get('contraseña')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(lista_persona)
    else:
        form = authenticationForm()
        return render(request, 'accounts/Login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('lista_persona')
    
# Create your views here.
