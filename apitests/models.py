from django.db import models


# Create your models here.
class Bakery(models.Model):
    name = models.CharField(max_length=225)


class Owner(models.Model):
    bakery = models.ForeignKey('apitests.Bakery', related_name='owners', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
