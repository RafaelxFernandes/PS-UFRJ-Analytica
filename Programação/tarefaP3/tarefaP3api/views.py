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

from datetime import date, datetime


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
        return JsonResponse("Ausência do parâmetro 'i'. Necessário acrescentar pelo menos 1 ingrediente", safe=False)

    # Mensagem de erro caso o parâmetro "q" não tenha sido passado
    if 'q' not in request.GET:
        return JsonResponse("Ausência do parâmetro 'q'. Necessário acrescentar query", safe=False)

    # Caso ambos os parâmetros tenham sido passados corretamente
    else:

        # Pegando os parãmetros passados
        ingredients = request.GET['i']
        query = request.GET['q']

        # Utilizando a Recipe Puppy API
        url = "http://www.recipepuppy.com/api/?i=" + ingredients + "&q=" + query
        response = requests.get(url)
        data = response.json()

        # Pegando apenas as primeiras três receitas
        receitas = data["results"][0:3]

        # Formatando o JSON a ser retornado
        resultado = {
            'query': query,
            'ingredients': ingredients,
            'results': receitas
        }

        # Mensagem caso não haja receitas com os parâmetros passados pelo usuário
        if resultado["results"] == []:
            return JsonResponse("Não há receitas com os ingredientes e query passada.", safe=False)


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
# Recebe como parâmetros a data de aniversário da pessoa, e uma data aleatória
def calculate_age(birthdate, random_date):

    # Data de quando esse programa é executado
    today = date.today()
    # print(today)

    # Idade no dia de hoje
    age_now = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    # Idade na data aleatória passada
    age_then = random_date.year - birthdate.year - ((random_date.month, random_date.day) < (birthdate.month, birthdate.day))
    
    return [age_now, age_then]


# Rota POST /age    
@api_view(['POST'])
@parser_classes([JSONParser])

# Necessário por conta de erro CSRF no Insomnia
@csrf_exempt
def age(request, format=None):

    # Mensagem de erro caso não tenha sido passado um nome 
    if not "name" in request.data:
        return Response("Parâmetro name não foi passado.")

    # Mensagem de erro caso data de aniversário não tenha sido passada
    if not "birthdate" in request.data:
        return Response("Parâmetro birthdate não foi passado.")

    # Mensagem de erro caso a data de aniversário não esteja dividida por -
    if not "-" in request.data["birthdate"]:
        return Response("Erro no parâmetro birthdate. O formato das datas a serem passadas é YYYY-MM-DD.")

    # Mensagem de erro caso data aleatória não tenha sido passada
    if not "random_date" in request.data:
        return Response("Parâmetro random_date não foi passado.")

    # Mensagem de erro caso a data aleatória não esteja dividida por -
    if not "-" in request.data["random_date"]:
        return Response("Erro no parâmetro random_state. O formato das datas a serem passadas é YYYY-MM-DD.")
    

    name = request.data["name"]

    # Mensagem de erro caso uma string vazia tenha sido passada no parâmetro name
    if len(name) == 0:
        return Response("Erro no parâmetro name. Não é possível passar uma string vazia.")


    # O parâmetro birthdate é tratado como uma string no formato YYYY-MM-DD
    # Dessa forma, utilizo a função split para separar corretamente YYYY, MM e DD
    # Usando "-" como parâmetro para a divisão
    birthdate_year = int(request.data["birthdate"].split("-")[0]) # YYYY
    birthdate_month = int(request.data["birthdate"].split("-")[1]) # MM
    birthdate_day = int(request.data["birthdate"].split("-")[2]) # DD

    # Mensagem de erro caso o ano não tenha sido passado como primeiro na data de aniversário
    if len(str(birthdate_year)) < 4:
        return Response("Erro no parâmetro birthdate. O formato das datas a serem passadas é YYYY-MM-DD.")

    # Mensagem de erro caso o mês não tenha sido passado como segundo na data de aniversário
    if birthdate_month > 12:
        return Response("Erro no parâmetro birthdate. O formato das datas a serem passadas é YYYY-MM-DD, e o valor do mês passado é maior do que 12.")

    # Mensagem de erro caso o dia não tenha sido passado como terceiro na data de aniversário
    if birthdate_day > 31:
        return Response("Erro no parâmetro birthdate. O formato das datas a serem passadas é YYYY-MM-DD, e o valor do dia passado é maior do que 31.")


    # O parâmetro random_date, assim como o birthdate acima, é tratado como uma string no formato YYYY-MM-DD
    # Dessa forma, utilizo a função split para separar corretamente YYYY, MM e DD
    # Usando "-" como parâmetro para a divisão
    random_date_year = int(request.data["random_date"].split("-")[0]) # YYYY
    random_date_month = int(request.data["random_date"].split("-")[1]) # MM
    random_date_day = int(request.data["random_date"].split("-")[2]) # DD

    # Mensagem de erro caso o ano não tenha sido passado como primeiro na data aleatória
    if len(str(random_date_year)) < 4:
        return Response("Erro no parâmetro random_date. O formato das datas a serem passadas é YYYY-MM-DD.")

    # Mensagem de erro caso o mês não tenha sido passado como segundo na data aleatória
    if random_date_month > 12:
        return Response("Erro no parâmetro random_date. O formato das datas a serem passadas é YYYY-MM-DD, e o valor do mês passado é maior do que 12.")

    # Mensagem de erro caso o dia não tenha sido passado como terceiro na data aleatória
    if random_date_day > 31:
        return Response("Erro no parâmetro random_date. O formato das datas a serem passadas é YYYY-MM-DD, e o valor do dia passado é maior do que 31.")

    # Mensagem de erro caso a data aleatória passada não seja depois da data em que a requisição for feita
    if date(random_date_year, random_date_month, random_date_day) <= datetime.now().date():
        return Response("Erro no parâmetro random_state. Data passada não encontra-se após a data de hoje.")


    # Cálculo da idade que a pessoa tem no momento da requisição e que ela terá na data do futuro
    age_now, age_then = calculate_age(date(birthdate_year, birthdate_month, birthdate_day), date(random_date_year, random_date_month, random_date_day))

    quote = "Olá, " + name + "! Você tem " + str(age_now) + " anos e em " + str(random_date_day) + "/" + str(random_date_month) + "/" + str(random_date_year) + " você terá " + str(age_then) + " anos."
    
    response = {
        'quote': quote,
        'ageNow': age_now,
        'ageThen': age_then
    }

    return Response(response)