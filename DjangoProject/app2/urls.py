from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("week_day/", views.week_day, name="week_day_page"),
]