from django.db import models

class Autor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

   

class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    descricao = models.TextField(null=True, blank=True)  
    
    def __str__(self):
        return self.nome

class Livro(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    autores = models.ManyToManyField(Autor)
    codigo = models.CharField(max_length=20)
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to='livros/media', blank=True, null=True)
    ano = models.IntegerField()
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)
    valor = models.CharField(max_length=20, blank=True, null=True)
    descricao = models.TextField(null=True, blank=True)  


    def __str__(self):
        return self.nome


    