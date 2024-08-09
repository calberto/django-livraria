from django.urls import path 
from .views import (
    home,
    listar_categorias,
    listar_autores,
    listar_livros,
    detalhar_livro,
    cadastrar_livro,
    cadastrar_categoria,
    cadastrar_autor
)
urlpatterns = [
    path('', home, name='core_home'),
	path('livros/', listar_livros, name='core_listar_livros'),
	path('listar_categorias/', listar_categorias, name='core_listar_categorias'),
	path('listar_autores/', listar_autores, name='core_listar_autores'),
	path('livro/<int:id>/', detalhar_livro, name='core_detalhar_livro'),
    path('livro/new/', cadastrar_livro, name='core_cadastrar_livro'),
    path('livro/new/', cadastrar_categoria, name='core_cadastrar_categoria'),
    path('livro/new/', cadastrar_autor, name='core_cadastrar_autor'),
]


