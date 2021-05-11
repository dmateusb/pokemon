from rest_framework import serializers
from api.models import *



class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ("id_api", "specie" "height", "name", "weight")

class StatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stat
        fields = ("pokemon", "hp", "attack", "defense", "special_attack",
                  "special_defense", "speed")


class EvolutionChainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EvolutionChain
        fields = ("chain_link")

class SpecieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Specie
        fields = ("name", "evolution_chain")

class EvolvesToSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EvolvesTo
        fields = ("chain_link")

class ChainLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChainLink
        fields = ("evolves_to", "specie")


