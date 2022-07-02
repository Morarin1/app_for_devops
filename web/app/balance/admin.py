from django.contrib import admin

from balance.models import Account, Transfer

admin.site.register(Account)
admin.site.register(Transfer)
