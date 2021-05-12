from django.urls import path, include
from rest_framework import routers
from website.views import *

router = routers.DefaultRouter()

urlpatterns = [
    path('', login), 
    path('home/', home, name="home"),
    path('home/pokemon', home, name="pokemon"),
]
