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

class EvolutionChainViewSet(ModelViewSet):
    queryset = EvolutionChain.objects.all()
    serializer_class = EvolutionChainSerializer

class SpecieViewSet(ModelViewSet):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer

class EvolvesToViewSet(ModelViewSet):
    queryset = EvolvesTo.objects.all()
    serializer_class = EvolvesToSerializer

class ChainLinkViewSet(ModelViewSet):
    queryset = ChainLink.objects.all()
    serializer_class = ChainLinkSerializer
