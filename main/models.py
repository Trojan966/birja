from django.db import models
from django.contrib.auth.models import User


# Create your mo
class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    btc = models.CharField(max_length=20)
    eth = models.CharField(max_length=20)
    bnb = models.CharField(max_length=20)
    bch = models.CharField(max_length=20)
    utc = models.CharField(max_length=20)


class TransactionBtc(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    currency = models.CharField(max_length=5)
    method = models.CharField(max_length=60)
    status = models.CharField(max_length=60)
    date = models.DateTimeField()


class TransactionBnb(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    currency = models.CharField(max_length=5)
    method = models.CharField(max_length=60)
    status = models.CharField(max_length=60)
    date = models.DateTimeField()


class TransactionEth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    currency = models.CharField(max_length=5)
    method = models.CharField(max_length=60)
    status = models.CharField(max_length=60)
    date = models.DateTimeField()


class TransactionBch(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    currency = models.CharField(max_length=5)
    method = models.CharField(max_length=60)
    status = models.CharField(max_length=60)
    date = models.DateTimeField()


class TransactionUtc(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    currency = models.CharField(max_length=5)
    method = models.CharField(max_length=60)
    status = models.CharField(max_length=60)
    date = models.DateTimeField()

    def __str__(self):
        return self.user.username
