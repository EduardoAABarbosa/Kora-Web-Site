from rest_framework import viewsets
from core.api import serializers
from core import models

class DepoimentoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DepoimentoSerializer
    queryset = models.Depoimentos.objects.all()

class Redes_SociaisViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Redes_SociaisSerializer
    queryset = models.Redes_Sociais.objects.all()