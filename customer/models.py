from django.db import models
from restaurant.models import Dishes, CustomUser, Location, Restaurant


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    total = models.FloatField()
    paid_status = models.BooleanField(default=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    phone = models.FloatField()
    ready = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Orders'



class OrderItems(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete= models.CASCADE, null=True)
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    paid_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Order Items'



class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Rating'


