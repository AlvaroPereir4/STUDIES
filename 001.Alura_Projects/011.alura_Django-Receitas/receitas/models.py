from django.db import models
from datetime import datetime

class Receita(models.Model):
    nome_receita = models.CharField(max_length=200) # essa função define várias coisa. ai a gente definiu a quantidade de chars do titulo.
    ingredientes = models.TextField() #formato diferentes de inserção de texto
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)

