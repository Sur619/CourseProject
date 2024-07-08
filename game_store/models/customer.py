from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    favorite_games = models.ManyToManyField('game_store.Game', related_name='fans', default=None, blank=True)

    def __str__(self):
        return self.username
