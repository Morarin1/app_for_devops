from django.db import models


class Product(models.Model):
    # TODO: add category
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=300)

    def __str__(self):
        return str(self.name)
