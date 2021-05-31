# Tarefa de Programação - Grupo P3

### A tarefa do grupo P3 foi, utilizando as linguagens de programção Python e/ ou JavaScript, criar uma API que deve ter três rotas:

#### 1. GET /hello

#### 2. GET /recipe?i=< ingredients >&q=< query >

#### 3. POST /age

### O código fonte para a tarefa em si encontra-se em:
- https://github.com/RafaelxFernandes/PS-UFRJ-Analytica/blob/main/Programa%C3%A7%C3%A3o/tarefaP3/tarefaP3api/views.py

#### Para completar essa tarefa, eu utilizei a linguagem Python, a framework Django REST para a criação da API, e o programa Insomnia para realizar os testes das rotas. Por ter sido minha primeira vez trabalhando com essa framework, segui o seguinte tutorial:

- https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c

#### Nele, consta-se a criação de ambientes virtuais para a instalação da framework. Como não sei em que ambiente esse código poderá ser executado, seguem links de referência para a criação de ambientes virtuais em Python:

- https://docs.python.org/pt-br/3/library/venv.html
- https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/
- https://www.linode.com/docs/guides/create-a-python-virtualenv-on-ubuntu-18-04/


#### Após criado e entrado no ambiente virtual, é necessário instalar o Django.
```
pip install django
```

#### Após instalado o Django e clonado o repositório, é necessário entrar na pasta com as tarefas de programação e instalar a biblioteca 'requests' para o correto funcionamento das rotas criadas. Então, iniciar o servidor.

```
cd PS-UFRJ-Analytica/Programação/tarefaP3
pip install requests
python manage.py runserver
```

#### Com o servidor iniciado, podemos então realizar as requisições pedidas.

#### 1. GET /hello

Essa rota deve responder uma requisição GET com um JSON da seguinte estrutura:
```
{
    hello: "Olá mundo! Sou eu, < SEU NOME >!"
}
```

#### Resultado:
![get-hello](https://github.com/RafaelxFernandes/PS-UFRJ-Analytica/blob/main/Programa%C3%A7%C3%A3o/screenshots/get-hello.png)


#### 2. GET /recipe?i=< ingredients >&q=< query >
#### OBS: Para não tornar o conteúdo desse README muito extenso, foram omitidas as imagens dos testes com mensagens de erro. O código e descrição de cada uma podem ser encontrados no [código fonte](https://github.com/RafaelxFernandes/PS-UFRJ-Analytica/blob/main/Programa%C3%A7%C3%A3o/tarefaP3/tarefaP3api/views.py#L30).

Utilizando a [API do Recipe Puppy](http://www.recipepuppy.com/about/api/), essa rota deve responder uma requisição GET de argumentos i = ingredients e q = query com um JSON da seguinte estrutura (contendo apenas 3 receitas quaisquer):
```
GET /recipe?i=”ing1, ing3”&q=”Receita”
{
    query: “Receita”,
    ingredients: [“ing1”, “ing3”],
    results: [
        {
            "recipe": "Receita 1",
            "url": "url.para/receita1",
            "ingredients": "ing1, ing2, ing3"
        },
        {
            "recipe": "Receita 2",
            "url": "url.para/receita2",
            "ingredients": "ing1, ing3"
        },
        {
            "recipe": "Receita 3",
            "url": "url.para/receita3",
            "ingredients": "ing1, ing3, ing4"
        },
    ]

}
```

#### Resultado:
![get-recipe](https://github.com/RafaelxFernandes/PS-UFRJ-Analytica/blob/main/Programa%C3%A7%C3%A3o/screenshots/get-recipe.png)

#### 3. POST /age
#### OBS: Para não tornar o conteúdo desse README muito extenso, foram omitidas as imagens dos testes com mensagens de erro. O código e descrição de cada uma podem ser encontrados no [código fonte](https://github.com/RafaelxFernandes/PS-UFRJ-Analytica/blob/main/Programa%C3%A7%C3%A3o/tarefaP3/tarefaP3api/views.py#L75).

Essa rota deve responder uma requisição POST que contenha um body com a seguinte estrutura:
```
{
    name: “Nome Sobrenome”,
    birthdate: yyyy-mm-dd,
    date: YYYY-MM-DD
}
```

Com um JSON com a seguinte estrutura:
```
{
    quote: “Olá, Nome Sobrenome! Você tem X anos eem DD/MM/YYYY você terá Y anos.”,
    ageNow: X,
    ageThen: Y
}
```

Ou seja, recebe o nome de uma pessoa (name), sua data de nascimento (birthdate) e uma data qualquer no futuro (date) e retorna uma frase no formato indicado, com a idade X que a pessoa tem no momento da requisição e a idade Y que ela terá na data do futuro.

#### Resultado:
![post-age](https://github.com/RafaelxFernandes/PS-UFRJ-Analytica/blob/main/Programa%C3%A7%C3%A3o/screenshots/post-age.png)




### Referências:
- https://flaviocopes.com/error-unable-import-django-db/
- https://stackoverflow.com/questions/35019030/how-to-return-custom-json-in-django-rest-framework
- https://www.django-rest-framework.org/api-guide/views/#class-based-views
- https://www.edureka.co/community/73316/how-to-return-custom-json-in-django-rest-framework
- https://data-flair.training/blogs/django-views/
- https://simpleisbetterthancomplex.com/tutorial/2016/07/27/how-to-return-json-encoded-response.html
- https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html
- https://dev.to/yahaya_hk/how-to-populate-your-database-with-data-from-an-external-api-in-django-398i
- https://docs.python.org/pt-br/3/library/datetime.html
- https://www.django-rest-framework.org/api-guide/parsers/