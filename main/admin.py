from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Balance)
admin.site.register(TransactionUtc)
admin.site.register(TransactionBch)
admin.site.register(TransactionBnb)
admin.site.register(TransactionBtc)
admin.site.register(TransactionEth)