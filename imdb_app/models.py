from django.db import models
from django.db.models import RESTRICT
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):

    class Meta:
        db_table = 'movies'

    name = models.CharField(max_length=128)
    year = models.IntegerField()
    director = models.ForeignKey(to="Director", on_delete=RESTRICT, null=False, blank=True)
    description = models.TextField(null=True, blank=False)
    duration_in_min = models.IntegerField(null=True)
    fav_pat = models.CharField(max_length=128, null=True, blank=False)

    actors = models.ManyToManyField('Actor', through="MovieActor")

    def __str__(self):
        return f"{self.name}, Year: {self.year}"


class Director(models.Model):

    class Meta:
        db_table = 'directors'

    name = models.CharField(max_length=128)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.name}, birth year: {self.birth_date}'


class Review(models.Model):
    class Meta:
        db_table = 'reviews'

    movie = models.ForeignKey(to="Movie", on_delete=RESTRICT)
    rating = models.FloatField(
        validators=[
            MaxValueValidator(limit_value=10),
            MinValueValidator(limit_value=1)
        ]
    )

    review_date = models.DateField()
    review_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.movie.name}, Rating: {self.rating}, Date: {self.review_date}, Text: {self.review_text}"


class Actor(models.Model):

    class Meta:
        db_table = 'actors'

    name = models.CharField(max_length=256, db_column='name', null=False, blank=False)
    birth_year = models.IntegerField(db_column='birth_year', null=False, blank=False)

    movies = models.ManyToManyField(Movie, through="MovieActor")

    def __str__(self):
        return self.name

class MovieActor(models.Model):

    class Meta:
        db_table = 'movie_actors'

    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    salary = models.DateField()
    main_role = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return f'{self.actor.name}, in movie {self.movie.name}'


# https://github.com/JoshuaTree63/jb_movie
# https://github.com/valeria-a/python-tutorials/blob/main/django-0_1/django_movies-main/movies_app/models.py#L17
# https://docs.google.com/document/d/13SudsoB-jghUsZjVB2QeCvhqxaCN9HNNgEVozYPIoQ4/edit