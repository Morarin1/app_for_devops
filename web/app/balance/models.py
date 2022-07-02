from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Account(models.Model):
    first_name = models.CharField('first_name', max_length=200, null=True)
    last_name = models.CharField('last_name', max_length=200, null=True)
    email = models.CharField(max_length=100)

    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return f'{self.user.username} ${self.balance}'


class Transfer(TimeStampedModel):
    from_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='from_account'
    )

    to_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='to_account'
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.from_account.user.username} ' +\
               f'sent ${str(self.amount)} ' +\
               f'to {self.to_account.user.username}'
