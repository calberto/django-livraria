from django.shortcuts import redirect, render,get_object_or_404
from core.models import Autor, Categoria, Livro
from .forms import AutorForm, CategoriaForm, LivroForm
from django.http import JsonResponse
import imghdr
from django.http import HttpResponse

def home(request):
    context = {'mensagem' : 'Olá Ninho!'}
    return render(request, 'core/index.html', context)


def listar_categorias(request):
    categorias = Categoria.objects.all()
    form = CategoriaForm()
    data = {'categorias': categorias, 'form': form}
    return render(request, 'core/listar_categorias.html', data)

#função cadastrar categoria

def cadastrar_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_listar_categorias') 

def salvar_categoria(request):
    if request.method == 'POST':
        categoria_id = request.POST.get('categoria_id')
        if categoria_id:  # Edição de categoria existente
            categoria = get_object_or_404(Categoria, pk=categoria_id)
            form = CategoriaForm(request.POST, request.FILES, instance=categoria)
        else:  # Novo livro
            form = CategoriaForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('core_listar_categorias')  # Redireciona após salvar
    else:
        form = CategoriaForm()

    return render(request, 'categoria_form.html', {'form': form})

def detalhar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    data = {
        'nome': categoria.nome,
        'descricao': categoria.descricao
    }
    return JsonResponse(data)


def categoria_delete_confirm(request, categoria_pk):
    categoria = Categoria.objects.get(pk=categoria_pk)
    categoria.delete()
    return redirect('core_listar_categorias')	

def listar_autores(request):
    autores = Autor.objects.all()
    form = AutorForm()
    data = {'autores': autores, 'form': form}
    return render(request, 'core/listar_autores.html', data)

#função cadastrar autor

def salvar_autor(request):
    if request.method == 'POST':
        autor_id = request.POST.get('autor_id')
        if autor_id:  # Edição de autor existente
            autor = get_object_or_404(Autor, pk=autor_id)
            form = AutorForm(request.POST, request.FILES, instance=autor)
        else:  # Novo autor
            form = AutorForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('core_listar_autores')  # Redireciona após salvar
    else:
        form = AutorForm()

    return render(request, 'autor_form.html', {'form': form})

def detalhar_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    data = {
        'nome': autor.nome,
        
    }
    return JsonResponse(data)

def autor_delete_confirm(request, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)
    autor.delete()
    return redirect('core_listar_autores')	


def listar_livros(request):
    livros = Livro.objects.all()
    form = LivroForm()
    data = {'livros': livros, 'form': form}
    return render(request, 'core/listar_livros.html', data)

#função cadastrar livro
def salvar_livro(request):
    if request.method == 'POST':
        livro_id = request.POST.get('livro_id')
        if livro_id:  # Edição de livro existente
            livro = Livro.objects.get(pk=livro_id)
            form = LivroForm(request.POST, request.FILES, instance=livro)
        else:  # Novo livro
            form = LivroForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('core_listar_livros')  # Redireciona após salvar
    
    return render(request, 'livro_form.html', {'form': form})

def livro_update(request, id):
	data = {}
	livro = Livro.objects.All(id=id) 
	form = LivroForm(request.POST or None, instance=livro)
	data['livro'] = livro
	data['form'] = form
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('core_lista_livros')		
	else:	
		return render(request, 'core/update_livro.html', data)

def detalhar_livro(request, id):
    livro = Livro.objects.get(pk=id)
    data = {
        'nome': livro.nome,
        'codigo': livro.codigo,
        'quantidade': livro.quantidade,
        'valor': livro.valor,
        'imagem': livro.imagem.url if livro.imagem else None,  # Verifique se existe imagem
        'ano': livro.ano,
        'descricao': livro.descricao,
        'categoria': livro.categoria.id if livro.categoria else None  # Se houver uma categoria associada
    }
    return JsonResponse(data)

def livro_delete_confirm(request, livro_pk):
    livro = Livro.objects.get(pk=livro_pk)
    livro.delete()
    return redirect('core_listar_livros')	