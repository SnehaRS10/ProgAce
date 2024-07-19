from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm

def home(request):
    return render(request, 'home.html') 

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'app/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')
