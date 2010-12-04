from django.db import models

class AmountOwedFromUser(models.Model):
	amount_owed = models.FloatField(decimal_places=2)
	address = models.ForeignKey(Address)
	date_time_collected = models.DateTimeField()
