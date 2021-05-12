from django.core.checks.messages import Error
from api.models import *
from api.serializers import *
from rest_framework.response import Response
from rest_framework import status


def insert_specie(specie):

    specie_serial = SpecieSerializer(data=specie)
    if specie_serial.is_valid():
        specie_saved = specie_serial.save()
        return specie_saved
    return Response(specie_serial.errors, status=status.HTTP_400_BAD_REQUEST)


def insert_pokemon(pokemon, specie):

    pokemon["specie"] = specie.id
    pokemon_serial = PokemonSerializer(data=pokemon)
    if pokemon_serial.is_valid():
        pokemon_saved = pokemon_serial.save()
        return pokemon_saved

    return Response(pokemon_serial.errors, status=status.HTTP_400_BAD_REQUEST)


def insert_pokemon_stat(stat, pokemon):

    stat["pokemon"] = pokemon.id
    stat_serial = StatSerializer(data=stat)
    if stat_serial.is_valid():
        stat_saved = stat_serial.save()
        return stat_saved
        
    return Response(stat_serial.errors, status=status.HTTP_400_BAD_REQUEST)


def insert_pokemon_data(pokemon_data):

    specie = insert_specie(pokemon_data.specie)
    pokemon = insert_pokemon(pokemon_data.pokemon, specie)
    insert_pokemon_stat(pokemon_data.stat, pokemon)