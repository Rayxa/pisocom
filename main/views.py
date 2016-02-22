from django.shortcuts import render
from .forms import casaForm

def search(request):
	form = casaForm()
	return render(request, 'search.html', {'form': form})