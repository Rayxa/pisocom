from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from .form import casaForm
# Create your views here.
def newcasa(request):
    c = {}
    c.update(csrf(request)) #aun no se usa
    form = casaForm()
    return render_to_response('registrarcasa.html', {'form': form})