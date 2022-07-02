from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel

from balance.models import Account
from product.models import Product


class Post(TimeStampedModel, TitleDescriptionModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        ordering = ['-modified']

    def __str__(self):
        return f"{self.title} ${self.price}"
