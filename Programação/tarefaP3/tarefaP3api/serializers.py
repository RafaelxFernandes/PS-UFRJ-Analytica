# Arquivo para o processo de serialização 
# (consultar e converter valores do banco de dados em JSON)

from rest_framework import serializers
from .models import PersonAge


class PersonAgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonAge
        fields = ("name", "birthdate", "random_date")