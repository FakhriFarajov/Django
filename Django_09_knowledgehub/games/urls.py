from django.urls import path

from . import views

app_name = "games"

urlpatterns = [
    path("", views.home, name="home"),
    path("football/", views.football, name="football"),
    path("hockey/", views.hockey, name="hockey"),
    path("basketball/", views.basketball, name="basketball"),
]
