from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


USER_TYPE = (
    ('1', 'restaurant'),
    ('2', 'customer'),
    ('3', 'partner'),
    ('4', 'staff'),
    ('5', 'none')
)


class CustomUser(AbstractUser):
    kind = models.CharField(max_length=30, choices=USER_TYPE, default='5')


