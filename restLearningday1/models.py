from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    