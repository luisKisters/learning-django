from django.db import models

class Product1(models.Model):
    title = models.TextField()
    price = models.IntegerField()
    description = models.TextField()