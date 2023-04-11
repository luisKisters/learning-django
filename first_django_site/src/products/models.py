from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) # max_length is required
    description = models.TextField(blank=True, null=True)
    price       = models.TextField()
    summary     = models.TextField(blank=True, null=False) # If blank is set to True, it makes it so that the field is required
    feature     = models.BooleanField()