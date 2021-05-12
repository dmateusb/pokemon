from django.core.checks.messages import Error
from api.models import *
from api.serializers import *

def insert_specie(specie):
    specie = SpecieSerializer(data=specie)
    if specie.is_valid():
        specie.save()
        return specie.data

    return specie.errors

def insert_pokemon_data(pokemon_data):
    specie = insert_specie(pokemon_data.specie)