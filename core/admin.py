from django.contrib import admin

# Register your models here.
from .models import LivrariaAutor, LivrariaCategoria, LivrariaLivro, LivrariaLivroAutor

class LivroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'valor', 'view_name_categoria', 'get_autores']
    search_fields = ['nome'] #pesquisa por nome
    list_filter = ['ano'] #filtrar por ano

    @admin.display(ordering='view_name_categoria')
    def view_name_categoria(self, obj):
        return obj.categoria.nome
        
    def get_autores(self, obj):
        for autor in obj.autor.all():
            return autor.nome
            #return [autor|.nome for autor in obj.autor.all()]	


admin.site.register(LivrariaAutor)
admin.site.register(LivrariaCategoria)
admin.site.register(LivrariaLivro)
admin.site.register(LivrariaLivroAutor)
