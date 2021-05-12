from django.shortcuts import render, redirect
import requests
from api.models import *
# Create your views here.


def login(request):
    return redirect(to='login/')

def home(request):
    if request.method == "POST":
        id = request.POST["id"]
        response = requests.get("https://pokeapi.co/api/v2/pokemon/"+id).json()
        pokemon = {"id_api": id, "specie": response["species"],
        "name":response["name"], "height":response["height"], "weight":response["weight"]}
        response = requests.get(pokemon["specie"]["url"]).json()
        specie = {"name": response["name"], 
        "evolution_chain": response["evolution_chain"]["url"]}
        print(specie)
    return render(request, 'home.html')
