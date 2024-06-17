from django.db import models


GENRE_CHOICES = [
    ('ACTION', 'Action'),
    ('DRAMA', 'Drama'),
    ('COMEDY', 'Comedy'),
    ('HORROR', 'Horror'),
    ('ROMANCE', 'Romance'),
]

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    watched = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
