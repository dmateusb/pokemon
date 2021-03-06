from django.urls import path, include
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register(r'stats', StatViewSet)
router.register(r'pokemons', PokemonViewSet)
router.register(r'species', SpecieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
