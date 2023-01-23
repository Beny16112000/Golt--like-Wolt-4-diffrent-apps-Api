from django.db import models
from customer.models import Order
from authentication.models import CustomUser


# Create your models here.


class Partner(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    available = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Partner'



class Delivery(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    on_way = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Delivery'


