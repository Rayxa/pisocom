from django.shortcuts import render_to_response
from .form import formCrearCasa

# Create your views here.
def crear_casa(request):
    if request.method == "POST":
        form = formCrearCasa(request.POST)
        if form.is_valid():
            casa = form.save(commit=True)
            casa.author = request.user
            casa.save()
            return redirect('main.views.creada')
    else:
        form = formCrearCasa()
    return render_to_response('crearCasa.html', {'form': form})