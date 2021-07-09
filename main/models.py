from django.db import models
from django.contrib.auth.models import User
# Create your mo
class Balance(models.Model):
    btc = models.CharField(max_length=20)
    eth = models.CharField(max_length=20)
    bch = models.CharField(max_length=20)
    lth = models.CharField(max_length=20)
class Transaction(models.Model):
    user = models.CharField(max_length=40)
    amount = models.FloatField()
    currency = models.CharField(max_length=5)
    method = models.CharField(max_length=60)
    status = models.CharField(max_length=60)
    date = models.DateTimeField()

    def __str__(self):
        return self.user.username

