from django.forms import ModelForm
from core.models import Autor, Categoria, Livro

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'codigo', 'quantidade', 'ano', 'valor', 'descricao', 'autores', 'categoria','imagem',]


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
