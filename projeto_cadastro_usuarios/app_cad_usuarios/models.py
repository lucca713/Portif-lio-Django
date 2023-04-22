from django.db import models

#tabela do BD precisa ser atualizada sempre q mudar algum item ou nome, ai atualiza com o comando manage
class Usuario(models.Model):
    #campo de indeitificação unico, aqui ele determina as coluna que vai ter no banco de dados, com os seu nomes
    #vai receber uma coluna id_usuario e uma nome e outra idade
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
