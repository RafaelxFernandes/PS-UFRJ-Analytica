from django.shortcuts import render
from django.http import JsonResponse

# Tarefa 1
# Rota GET /hello
# Retorna o seguinte JSON
# {
#   'hello': "Olá mundo! Sou eu, Rafael Fernandes!"
# }
def hello(request):
    data = { 'hello': 'Olá mundo! Sou eu, Rafael Fernandes!' }
    return JsonResponse(data)