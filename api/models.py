from django.db import models

# Create your models here.


class Specie(models.Model):
    name = models.CharField(max_length=30)
    evolution_chain = models.URLField()

    def __str__(self):
        return 'id: {}, name: {}, evolution_chain: {}'.format(
            self.id, self.name, self.evolution_chain)


class Pokemon(models.Model):
    id_api = models.IntegerField()
    name = models.CharField(max_length=30)
    height = models.IntegerField()
    weight = models.IntegerField()
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)

    def __str__(self):
        return 'id:{} | id_api: {} | specie: {} | height: {} | name: {} | weight: {}'.format(
            self.id, self.id_api, self.specie.name, self.height, self.name, self.weight
        )


class Stat(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()

    def __str__(self):
        return """pokemon_id: {} | hp: {} | attack: {} | defense: {}
         | special_attack: {} | special_defense: {} | speed: {}""".format(
            self.pokemon.id, self.hp, self.attack, self.defense,
            self.special_attack, self.special_defense, self.speed
        )
