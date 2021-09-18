from rest_framework import serializers
from core import models

class DepoimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Depoimentos
        fields='__all__'

class Redes_SociaisSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Redes_Sociais
        fields='__all__'