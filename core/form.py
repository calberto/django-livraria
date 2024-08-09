from django.forms import ModelForm
from core.models import LivrariaLivro, LivrariaCategoria, LivrariaAutor

class LivroForm(ModelForm):
    class Meta:
        model = LivrariaLivro
        fields = '__all__'

class CategoriaForm(ModelForm):
    class Meta:
        model = LivrariaCategoria
        fields = '__all__'

class AutorForm(ModelForm):
    class Meta:
        model = LivrariaAutor
        fields = '__all__'
