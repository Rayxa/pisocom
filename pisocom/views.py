from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.contrib import auth
from . import forms

# Iniciar sesión
def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('accounts/login.html',c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username,password=password)
	if user is not None:
		auth.login(request, user)
		return redirect('home')
	else:
		return redirect('invalid')

def loggedin(request):
	return render_to_response('accounts/loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
	return render_to_response('accounts/invalid_login.html')

# Cerrar sesión
def logout(request):
	auth.logout(request)
	return render_to_response('accounts/logout.html')

# Registrar un nuevo usuario
def register(request):
	if request.method == "POST":
		form = forms.RegistrationForm(request.POST);
		if form.is_valid():
			new_user = form.save(commit=True)
			return redirect('register_success')
	else:
		form = forms.RegistrationForm();
	return render(request, 'accounts/register/register.html', {'form': form})

def user_created(request):
	return render(request, 'accountsr/register/user_created.html', {})
