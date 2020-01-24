from django.db import models

class Especie(models.Model):
    nome = models.CharField(max_length=256, verbose_name='Nome', blank=False, null=False)

class Imagem(models.Model):
    caminho = models.ImageField(verbose_name='caminho', upload_to='imagens/')

class Acesso(models.Model):
    nome = models.CharField(max_length=256, verbose_name='Nome', blank=False, null=False)
    especie = models.OneToOneField(Especie, on_delete='cascade')
    imagem = models.ManyToManyField(Imagem)



