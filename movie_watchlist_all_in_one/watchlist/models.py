from django.conf.global_settings import AUTH_USER_MODEL
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

STATUS_CHOICES = [
    ('to_watch', 'to watch'),
    ('watching', 'currently watching'),
    ('watched', 'watched'),
]

# Create your models here.
class Movie(models.Model):
    global STATUS_CHOICES
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='to_watch'
    )
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

