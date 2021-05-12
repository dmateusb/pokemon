from django.shortcuts import render, redirect
import requests
from api.models import *
from api.util import *
from .util.data import *
# Create your views here.


def login(request):
    return redirect(to='login/')

def home(request):
    if request.method == "POST":
        id = request.POST["id"]
        pokemon_data = Data()
        pokemon_data.set_all_data(id)
        insert_pokemon_data(pokemon_data)

    return render(request, 'home.html')
