from django.urls import path
from django.conf.urls.static import static
from . import views
# from core import settings

from . import views # arquivo views que ainda não utilizamos

urlpatterns = [
	path('', views.listar_livros, name='listar_livros'),
	path('listar_categorias', views.listar_categorias, name='listar_categorias'),
	path('listar_autores', views.listar_autores, name='listar_autores'),
	path('livro/<int:id>/', views.detalhar_livro, name='detalhar_livro'),
]

