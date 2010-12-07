from django.db import models
from address.address import Address

class AmountOwedFromUser(models.Model):
	amount_owed = models.FloatField()
	address = models.ForeignKey(Address)
	date_time_collected = models.DateTimeField()
