from django.shortcuts import render, redirect
import requests
from api.models import *
from api.util import *
from .util.data import *

#Check if the pokemon to consult is already in the database

def pokemon_in_database(id):
    try:
        listing = Pokemon.objects.get(id_api=id)
    except Pokemon.DoesNotExist:
        listing = None
    return True if listing != None else False

#Search pokemon, specie and stats in the Pokeapi

def search_pokemon(id):
    pokemon_data = Data()
    pokemon_data.set_all_data(id)
    insert_pokemon_data(pokemon_data)
    return pokemon_data

#Get the pokemon, specie and stats from the local database

def get_pokemon(id):
    pokemon_data = Data()
    pokemon_data.get_all_data(id)
    return pokemon_data

#Verify what is the kinds of evolution that the pokemon
#may have

def verify_kind_evolution(pokemon, evolution_chain):
    columnas = []
    len_chain = len(evolution_chain)
    pokemon_name = pokemon["name"]
    have_evolution = True if len_chain > 1 else False
    if have_evolution:
        for i in range(len(evolution_chain)):
            if pokemon_name == evolution_chain[i]:
                evolution_chain.pop(i)
                pokemon_index = i
                break
        if len_chain == 2:
            if pokemon_index == 0:
                columnas.append("Evolución")
            else:
                columnas.append("Involución")
        else:
            if pokemon_index == 0:
                columnas.append("Evolucion")
                columnas.append("Evolucion(2)")
            elif pokemon_index == 1:
                columnas.append("Involucion")
                columnas.append("Evolucion")
            else:
                columnas.append("Involucion(2)")
                columnas.append("Involucion")
    return columnas, evolution_chain


def login(request):
    return redirect(to='login/')


def home(request):

    return render(request, 'home.html')

#the main methof for search a Pokemon

def search(request):

    if request.method == "GET":
        id = request.GET["id"]
    else:
        id = request.POST["id"]


    if not pokemon_in_database(id):
        data = search_pokemon(id)
        pokemon = data.pokemon
    else:
        data = get_pokemon(id)
        pokemon = data.pokemon

    columnas, evolution_chain = verify_kind_evolution(
        pokemon, data.evolution_chain)

    ctx = {"id_api": pokemon["id_api"], "name": pokemon["name"],
           "height": pokemon["height"], "weight": pokemon["weight"],
           "specie": data.specie["name"], "columnas": columnas,
           "evolution_chain": evolution_chain}
    return render(request, 'pokemon.html', ctx)
