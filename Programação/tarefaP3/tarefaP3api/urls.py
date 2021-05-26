# Arquivo para rotas URL

from django.urls import include, path
from rest_framework import routers
from . import views

rota = routers.DefaultRouter()

# Rotas
# Tarefa 1 - /hello
rota.register(r'hello', views.NomeViewSet)

urlpatterns = [
    path('', include(rota.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]