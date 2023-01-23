from django.db import models
from authentication.models import CustomUser


# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=90)

    class Meta:
        verbose_name_plural = 'Location'



class Restaurant(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media/restaurant_images')
    category = models.CharField(max_length=40)
    detail = models.TextField(blank=True)
    website = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Restaurants'



class Dishes(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name  = models.CharField(max_length=124)
    img = models.ImageField(upload_to='media/dishes_images')
    detail = models.TextField(blank=True)
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Dishes'



class Open(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    available = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Available'


        