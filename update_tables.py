import csv
import datetime
import os
import django
from django.db.models import Q, Count, Min, Max, Avg

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()

from imdb_app.models import *
import imdb_app.models

def create_movie(movie_name:str, movie_year: int, director: imdb_app.models.Director=None, movie_description=None):
    movie = Movie.objects.create(
        name=movie_name,
        year=movie_year,
        director=director,
        description=movie_description
    )
    return movie