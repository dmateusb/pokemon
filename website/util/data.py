from api.models import Pokemon
from api.util import *
import requests


class Data:

    def __init__(self):
        self.pokemon = None
        self.stat = None
        self.specie = None
        self.evolution_chain = []

    def set_pokemon(self, id):
        pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/"+id).json()
        self.pokemon = {"id_api": int(id), "name": pokemon["name"],
                        "height": pokemon["height"], "weight": pokemon["weight"]}
        return pokemon

    def set_stat(self, pokemon):
        stats = pokemon["stats"]
        self.stat = {"hp": stats[0]["base_stat"], "attack": stats[1]["base_stat"],
                     "defense": stats[2]["base_stat"], "special_attack": stats[3]["base_stat"],
                     "special_defense": stats[4]["base_stat"], "speed": stats[5]["base_stat"]}

    def set_specie(self, pokemon):
        specie = requests.get(pokemon["species"]["url"]).json()
        self.specie = {"name": specie["name"],
                       "evolution_chain": specie["evolution_chain"]["url"]}

    def set_evolution_chain(self):
        # Get the evolution chain
        response = requests.get(self.specie["evolution_chain"]).json()
        chain = response["chain"]
        while len(chain["evolves_to"]) != 0:
            self.evolution_chain.append(chain["species"]["name"])
            chain = chain["evolves_to"][0]
        self.evolution_chain.append(chain["species"]["name"])

    def get_pokemon(self, id):
        pokemon_result = Pokemon.objects.get(id_api=id)
        pokemon_id = pokemon_result.pk
        pokemon_serializer = PokemonSerializer(pokemon_result, many=False)
        self.pokemon = pokemon_serializer.data
        return pokemon_id

    def get_stat(self, id):
        stat_result = Stat.objects.get(pokemon=id)
        stat_serializer = StatSerializer(stat_result, many=False)
        self.stat = stat_serializer.data

    def get_specie(self, id):
        specie_result = Specie.objects.get(pokemon=id)
        specie_serializer = SpecieSerializer(specie_result, many=False)
        self.specie = specie_serializer.data

    def set_all_data(self, id):
        pokemon = self.set_pokemon(id)
        self.set_stat(pokemon)
        self.set_specie(pokemon)
        self.set_evolution_chain()

    def get_all_data(self,id):
        pokemon_id = self.get_pokemon(id)
        self.get_stat(pokemon_id)
        self.get_specie(pokemon_id)
        self.set_evolution_chain()
