from django.shortcuts import render
from django.http import JsonResponse

# Foi necessário rodar no terminal o comando
# pip install requests
import requests


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
    elif 'q' not in request.GET:
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