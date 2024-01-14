from django.db import models

class Product(models.Model):
    name = models.CharField(blank=False, max_length=255)
    buyed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

