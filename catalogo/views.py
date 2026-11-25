from django.shortcuts import get_object_or_404, render
from .models import Libro, Autor

# Create your views here.
def principal (request):
    context = Libro.objects.all()
    return render(request,'catalogo/principal.html', {'libros':context})

def detalle_libro (request, pk):
    context = get_object_or_404(Libro, pk=pk)
    return render(request,'catalogo/detalle_libro.html', {'libro':context})

def autor(request, pk):
    autor= get_object_or_404(Autor, pk=pk)
    return render(request, 'catalogo/autor.html', {'autor':autor})