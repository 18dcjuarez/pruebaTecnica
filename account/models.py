from django.db import models


class Account(models.Model):
    account = models.CharField(max_length=15, blank=False, editable=False)
    balance = models.FloatField(default=0)
    owner = models.CharField(max_length=15, blank=False, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
