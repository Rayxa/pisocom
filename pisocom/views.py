from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from . import forms

def register(request):
	if request.method == "POST":
		form = forms.RegistrationForm(request.POST);
		if form.is_valid():
			new_user = form.save(commit=True)
			return redirect('pisocom.views.user_created')
	else:
		form = forms.RegistrationForm();
	return render(request, 'pisocom/register.html', {'form': form})

def user_created(request):
	return render(request, 'pisocom/user_created.html', {})
