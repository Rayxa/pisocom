from django.shortcuts import render, redirect
from .forms import casaForm
from .models import casa
from django.http import HttpResponse


'''
casas = casa.objects.filter(title__contains='casa')
return render(request, 'search_result.html', {'posts': casas})
'''

def search(request):
	if request.method == "POST":
		form = casaForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			casas = casa.objects.filter(title__contains=post.title)
			return render(request, 'search_result.html', {'casas': casas})
	else:
		form = casaForm()
	return render(request, 'search.html', {'form': form})