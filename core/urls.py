from django.urls import path

from .views import (
    home,
    listar_categorias,
    listar_autores,
    listar_livros,
    detalhar_livro,
    detalhar_autor,
    detalhar_categoria,
    livro_update,
    salvar_livro,
    salvar_categoria,
    salvar_autor,
    autor_delete_confirm,
    categoria_delete_confirm,
    livro_delete_confirm
)
urlpatterns = [
    path('', home, name='livros_home'),
	path('livros/', listar_livros, name='core_listar_livros'),
    path('livro_update/<int:id>/', livro_update, name='core_livro_update'),
	path('detalhar_livro/<int:id>/', detalhar_livro, name='detalhar_livro'),
    path('salvar_livro/', salvar_livro, name='core_salvar_livro'),
    path('livro_delete/<int:livro_pk>/', livro_delete_confirm, name='core_livro_delete_confirm'),


	path('listar_categorias/', listar_categorias, name='core_listar_categorias'),
    path('detalhar_categoria/<int:categoria_id>/', detalhar_categoria, name='sistema_detalhar_categoria'),
    path('salvar_categoria/', salvar_categoria, name='core_salvar_categoria'),
    path('categoria_delete/<int:categoria_pk>/', categoria_delete_confirm, name='core_categoria_delete_confirm'),


	path('listar_autores/', listar_autores, name='core_listar_autores'),
    path('detalhar_autor/<int:autor_id>/', detalhar_autor, name='sistema_detalhar_autor'),
    path('salvar_autor/', salvar_autor, name='core_salvar_autor'),
    path('autor_delete/<int:autor_pk>/', autor_delete_confirm, name='core_autor_delete_confirm'),

]

