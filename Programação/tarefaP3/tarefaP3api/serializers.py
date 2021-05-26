# Arquivo para o processo de serialização (consultar e converter
# valores do banco de dados em JSON)

from rest_framework import serializers

from .models import Nome


# Tarefa 1 - /hello
# Serializador para a model Nome
class NomeSerializador(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nome
        fields = ("id", "nome")

    def to_representation(self, instancia):
        json_formatado = super(NomeSerializador, self).to_representation(instancia)
        novo_campo = {"hello": "Olá, mundo! Sou eu, self.fields[-1] !"}
        json_formatado.update(novo_campo)
        
        return json_formatado