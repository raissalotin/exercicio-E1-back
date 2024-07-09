from django.db import models

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)