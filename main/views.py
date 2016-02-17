from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import RegistrationForm

def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST);
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.save();
			return redirect('main.views.user_created')
	else: 
		form = RegistrationForm();
	return render(request, 'pisocom/register.html', {'form': form})

def user_created(request):
	return render(request, 'pisocom/user_created.html', {})