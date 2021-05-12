from rest_framework import serializers
from api.models import *



class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ("id_api", "name", "height", "weight", "specie")

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ("pokemon", "hp", "attack", "defense", "special_attack",
                  "special_defense", "speed")

class SpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = ("name", "evolution_chain")