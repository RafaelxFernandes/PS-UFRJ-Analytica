from django.shortcuts import render
from rest_framework import viewsets

from .serializers import NomeSerializador
from .models import Nome


# Tarefa 1 - /hello
# View para a model Nome
# Mostra "Olá mundo! Sou eu, <SEU NOME>!"
class NomeViewSet(viewsets.ModelViewSet):
    queryset = Nome.objects
    serializer_class = NomeSerializador