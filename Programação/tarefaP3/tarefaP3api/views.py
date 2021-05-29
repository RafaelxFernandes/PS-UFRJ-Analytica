# -*- coding: utf-8 -*-

# Foi necessário rodar no terminal o comando
# pip install requests
import requests
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response


from datetime import date


# Tarefa 1
# Rota GET /hello
# Retorna o seguinte JSON
# {
#   'hello': "Olá mundo! Sou eu, Rafael Fernandes!"
# }
def hello(request):
    data = { 'hello': 'Olá mundo! Sou eu, Rafael Fernandes!' }
    return JsonResponse(data)


# Tarefa 2
# Rota GET /recipe?i=<ingredients>&q=<query>
# Utilizando Recipe Puppy API
# Responde uma requisição GET de argumentos i = ingredientes e q = query com um JSON
# contendo apenas 3 receitas quaisquer
def recipe(request):

    # Mensagem de erro caso o parâmetro "i" não tenha sido passado
    if 'i' not in request.GET:
        return JsonResponse("Necessário acrescentar pelo menos 1 ingrediente", safe=False)

    # Mensagem de erro caso o parâmetro "q" não tenha sido passado
    if 'q' not in request.GET:
        return JsonResponse("Necessário acrescentar query", safe=False)

    # Caso ambos os parâmetros tenham sido passados corretamente
    else:

        # Pegando os parãmetros passados
        ingredients = request.GET['i']
        query = request.GET['q']

        # Recipe Puppy API
        url = "http://www.recipepuppy.com/api/?i=" + str(ingredients) + "&q=" + str(query)
        response = requests.get(url)
        data = response.json()

        # Apenas as primeiras três receitas
        receitas = data["results"][0:3]

        # Formatando o JSON a ser retornado
        resultado = {
            'query': query,
            'ingredients': ingredients,
            'results': receitas
        }

        return JsonResponse(resultado)


# Tarefa 3
# Rota POST /age
# Recebe o nome de uma pessoa (name), sua datade nascimento (birthdate) 
# e uma data qualquer no futuro (date) 
# Retorna o JSON com a idade X que a pessoa tem no momento da requisição 
# e a idade Y que ela terá na data do futuro.
# {
#   quote: “Olá, Nome Sobrenome! Você tem X anos e em DD/MM/YYYY você terá Y anos.”,
#   ageNow: X,
#   ageThen: Y
# }

# Função para calcular a idade em anos
# Recebe como parâmetros a data de aniversário da pessoa, e uma data qualquer
def calculate_age(birthdate, random_date):

    # Data de quando esse programa é executado
    today = date.today()
    # print(today)

    # Idade no dia de hoje
    age_now = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    # Idade na data qualquer passada
    age_then = random_date.year - birthdate.year - ((random_date.month, random_date.day) < (birthdate.month, birthdate.day))
    
    return [age_now, age_then]


# Rota POST /age    
@api_view(['POST'])
@parser_classes([JSONParser])

# Necessário por conta de erro CSRF no Insomnia
@csrf_exempt
def age(request, format=None):
    
    return Response({'received data': request.data})