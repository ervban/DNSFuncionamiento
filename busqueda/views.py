from django.shortcuts import render, redirect
from .models import Paginas

def home(request):    
    paginasListado = Paginas.objects.all()
    return render(request, "busqueda/Buscador.html", {"pagina": paginasListado})



def buscar(request):
    query = request.GET.get('q')  # Obtener el valor de búsqueda del parámetro 'q' en la URL
    paginasListado = None

    if query:  # Si se proporciona un valor de búsqueda
        paginasListado = Paginas.objects.filter(Nombre__icontains=query) | Paginas.objects.filter(ip_nombre__icontains=query)
    else:
        paginasListado = Paginas.objects.all()
    return render(request, "busqueda/Buscador.html", {"pagina": paginasListado})