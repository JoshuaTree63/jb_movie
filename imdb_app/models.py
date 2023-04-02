from django.db import models
from django.db.models import RESTRICT
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):

    class Meta:
        db_table = 'movies'

    name = models.CharField(max_length=128)
    year = models.IntegerField()
    director = models.ForeignKey(to="Director", on_delete=RESTRICT, null=False, blank=True)
    description = models.TimeField(null=True, blank=False)
    duration_in_min = models.IntegerField(null=True)

    actors = models.ManyToManyField('Actor', through="MovieActor")

    def __str__(self):
        return f"{self.name}, Year: {self.year}"


class Director(models.Model):

    class Meta:
        db_table = 'directors'

    name = models.CharField(max_length=128)



# https://github.com/JoshuaTree63/jb_movie
# https://github.com/valeria-a/python-tutorials/blob/main/django-0_1/django_movies-main/movies_app/models.py#L17
# https://docs.google.com/document/d/13SudsoB-jghUsZjVB2QeCvhqxaCN9HNNgEVozYPIoQ4/edit