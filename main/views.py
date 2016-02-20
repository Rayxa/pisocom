from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
from .form import formCrearCasa, formDireccion

def crear_casa(request):
    if request.method == "POST":
        form = formCrearCasa(request.POST)
        if form.is_valid():
            casa = form.save(commit=True)
            casa.propietario = request.user
            casa.save()
            return HttpResponseRedirect('/casa_creada')
    else:
        form = formCrearCasa()
    return render(request, 'crear_casa.html', {'form': form})

def casa_creada(request):
    return render_to_response('casa_creada.html')
	
def crear_direccion(request):
    if request.method == "POST":
        form = formDireccion(request.POST)
        if form.is_valid():
            dir = form.save(commit=True)
            dir.usuario = request.user
            dir.save()
            return HttpResponseRedirect('/crear_casa')
    else:
        form = formDireccion()
    return render(request, 'crear_direccion.html', {'form': form})