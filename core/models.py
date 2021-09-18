from django.db import models

class Depoimentos(models.Model):
    nome=models.CharField('Nome',max_length=100)
    cargo=models.CharField('Cargo',max_length=100)
    foto=models.ImageField('Foto',upload_to='foto')
    depoimento=models.CharField('Depoimento',max_length=250)

class Redes_Sociais(models.Model):
    facebook=models.CharField('Facebook',max_length=100)
    twitter=models.CharField('Twitter',max_length=100)
    pinterest=models.CharField('Pinterest',max_length=100)
    instagram=models.CharField('Instagram',max_length=100)