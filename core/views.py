from django.shortcuts import redirect, render,get_object_or_404
from core.models import LivrariaAutor, LivrariaCategoria, LivrariaLivro, LivrariaLivroAutor
from .form import LivroForm

def home(request):
    context = {'mensagem':'Olá Ninho' }
    return render(request, 'core/index.html', context)

#função cadastrar livro
def cadastrar_livro(request, id):
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            livro = form.save(commit=False)
            form.save()
            return redirect('detalhar_livro', id=livro.id)
    else:
        form = LivroForm()
    return render(request, 'livraria/editar_livro.html', {'form': form})

#função cadastrar livro
def cadastrar_livro(request, id):
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            livro = form.save(commit=False)
            form.save()
            return redirect('detalhar_livro', id=livro.id)
    else:
        form = LivroForm()
    return render(request, 'livraria/editar_livro.html', {'form': form})
#função cadastrar categoria
def cadastrar_categoria(request, id):
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            categoria = form.save(commit=False)
            form.save()
            return redirect('detalhar_categoria', id=categoria.id)
    else:
        form = LivroForm()
    return render(request, 'livraria/editar_categoria.html', {'form': form})

#função cadastrar livro
def cadastrar_autor(request, id):
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            autor = form.save(commit=False)
            form.save()
            return redirect('detalhar_autor', id=autor.id)
    else:
        form = LivroForm()
    return render(request, 'livraria/editar_autor.html', {'form': form})


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
