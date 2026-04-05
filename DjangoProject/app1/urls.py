from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("say_hello/", views.say_hello, name="say_hello_page"),
]