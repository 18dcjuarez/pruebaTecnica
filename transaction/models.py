from django.db import models


class Transaction(models.Model):
    fromAccount = models.CharField(max_length=15, blank=False, editable=False)
    toAccount = models.CharField(max_length=15, blank=False, editable=False)
    amount = models.FloatField(default=0)
    sentAt = models.DateTimeField(auto_now_add=True, editable=False)