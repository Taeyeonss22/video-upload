from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationUser

# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Cuenta mala')
            else:
                return HttpResponse('invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        user_form = RegistrationUser(request.POST)
        if user_form.is_valid():
            usuario = user_form.save(commit=False)
            usuario.set_password(user_form.cleaned_data['password'])
            usuario.save()
            return render(request, 'account/register_done.html', {'usuario':usuario})
    else:
        user_form = RegistrationUser()
    return render(request, 'account/register.html', {'user_form':user_form})
