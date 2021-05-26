from django.db import models


# Tarefa 1 - /hello
# Banco de dados com nomes de pessoas
class Nome(models.Model):
    nome = models.CharField(max_length = 60)

    def __str__(self):
        return self.nome
