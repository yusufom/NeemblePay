from django.db import models
from auth.models import User

# Create your models here.


class ATM(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)
    expiring_date = models.CharField(max_length=20)
    atm_type = models.CharField(max_length=100)
    ccv = models.CharField(max_length=100)

    def __str__(self):
        return self.user