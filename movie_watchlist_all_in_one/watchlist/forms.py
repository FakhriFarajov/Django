from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from watchlist import models

class CreateMovieForm(forms.Form):
    title = forms.CharField(max_length=255)
    genre = forms.CharField(max_length=255)
    release_year = forms.IntegerField()
    rating = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    status = forms.ChoiceField(choices=models.STATUS_CHOICES)


class UpdateMovieForm(forms.Form):
    title = forms.CharField(max_length=255)
    genre = forms.CharField(max_length=255)
    release_year = forms.IntegerField()
    rating = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    status = forms.ChoiceField(choices=models.STATUS_CHOICES)
