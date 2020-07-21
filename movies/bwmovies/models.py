from django.db import models

# Create your models here.
class dongzuopian(models.Model):
    movie_type = models.CharField(max_length=30)
    movie_name = models.CharField(max_length=100)
    movie_star = models.CharField(max_length=30)
    movie_actor = models.CharField(max_length=100)
    movie_url = models.CharField(max_length=100)
    movie_img = models.CharField(max_length=100)