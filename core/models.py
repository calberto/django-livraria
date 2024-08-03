from django.db import models


class LivrariaAutor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'livraria_autor'


class LivrariaCategoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'livraria_categoria'


class LivrariaLivro(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20)
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to='livros/', blank=True, null=True)
    ano = models.IntegerField()
    categoria = models.ForeignKey(LivrariaCategoria, models.DO_NOTHING)
    valor = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome


    class Meta:
        managed = False
        db_table = 'livraria_livro'


class LivrariaLivroAutor(models.Model):
    id = models.BigAutoField(primary_key=True)
    livro = models.ForeignKey(LivrariaLivro, models.DO_NOTHING)
    autor = models.ForeignKey(LivrariaAutor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'livraria_livro_autor'
        unique_together = (('livro', 'autor'),)
