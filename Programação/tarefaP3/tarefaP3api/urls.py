# Arquivo para rotas URL

from django.urls import include, path
from . import views

# Rotas

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Tarefa 1
    # Rota GET /hello
    path('hello', views.hello, name = "hello"),

    # Tarefa 2
    # Rota GET /recipe
    path('recipe', views.recipe, name = "recipe"),
]