from django.contrib import admin
from api.models import *
# Register your models here.


admin.site.register(Stat)
admin.site.register(Pokemon)
admin.site.register(EvolutionChain)
admin.site.register(Specie)
admin.site.register(EvolvesTo)
admin.site.register(ChainLink)