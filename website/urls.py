from django.urls import path, include
from rest_framework import routers
from website.views import home

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)), 
    path('home/', home, name="home")
]
