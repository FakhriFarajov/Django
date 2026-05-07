from django import forms

from watchlist import models

class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = ["title", "genre", "year", "status", "rating"]



class UpdateMovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = ["title", "genre", "year", "status", "rating"]

