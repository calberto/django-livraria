from django.shortcuts import render,get_object_or_404
from core.models import LivrariaAutor, LivrariaCategoria, LivrariaLivro, LivrariaLivroAutor

def listar_categorias(request):
    categorias = LivrariaCategoria.objects.all()
    return render(request, 'core/listar_categorias.html', {'categorias':categorias})

def listar_autores(request):
    autores = LivrariaAutor.objects.all()
    return render(request, 'core/listar_autores.html', {'autores':autores})

def listar_livros(request):
    livros = LivrariaLivro.objects.all()
    return render(request, 'core/listar_livros.html', {'livros':livros})

def detalhar_livro(request, id):
    livro = get_object_or_404(LivrariaLivro, pk=id)
    return render(request, 'core/detalhar_livro.html', {'livro':livro})

# Create your views here.
