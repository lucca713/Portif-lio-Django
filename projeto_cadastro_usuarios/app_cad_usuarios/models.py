from django.db import models

class Usuarios(models.Model):
    #campo de indeitificação unico
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(next_length=255)
    idade = models.IntegerField()
