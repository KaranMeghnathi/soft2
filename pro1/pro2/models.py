from email.policy import default

from django.db import models
# Create your models here.


class Rest(models.Model):
    id = models.IntegerField(primary_key= True)
    restaurant_name = models.CharField(default=" ", max_length=100)
    city = models.CharField(default=" ", max_length=100)
    img = models.ImageField(upload_to="static/assets/image", default=" ")


class Kenu(models.Model):

    restaurant_name = models.ForeignKey(Rest, on_delete=models.CASCADE)
    dish_name = models.CharField(default=' ', max_length=200)
    img = models.ImageField(upload_to='static/assets/image', default=' ')
    price = models.IntegerField(default=" ")



