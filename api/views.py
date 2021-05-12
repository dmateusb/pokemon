from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.models import *
from api.serializers import *


class StatViewSet(ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer

class PokemonViewSet(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class SpecieViewSet(ModelViewSet):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer