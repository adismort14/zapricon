from django.urls import path
from .views import *

app_name = "mess_menu"

urlpatterns = [
    path("", showMenu, name="showMenu"),
]
