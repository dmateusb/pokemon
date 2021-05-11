from django.urls import path, include
from rest_framework import routers
from authentication.views import *

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)), 
    path('register/', registerView, name="registerView"),
   # path('', include())
]
