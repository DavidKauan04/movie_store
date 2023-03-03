from django.db import models
from users.models import User
from users.serializers import UserSerializer

# Create your models here.

class RatingChoices(models.TextChoices):
    G = 'G',
    PG = 'PG',
    PG_13 = 'PG-13',
    NC_17 = 'NC-17'
    R = 'R',

class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    synopsis = models.TextField(null=True, default=None)
    rating = models.CharField(max_length=20, null=True, choices=RatingChoices.choices, default=RatingChoices.G)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
    )
    ordered_by = models.ManyToManyField('users.User', through='MovieOrder', related_name='movies_orders')


class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)