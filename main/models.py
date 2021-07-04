from django.db import models
from django.contrib.auth.models import User
# Create your mo
class Transaction(models.Model):
    user = models.CharField(max_length=40)
    amount = models.FloatField()
    currency = models.CharField(max_length=5)
    method = models.CharField(max_length=60)
    status = models.CharField(max_length=60)
    date = models.DateTimeField()

    def __str__(self):
        return self.user.username

