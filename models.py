from django.db import models
from address.zillow import zEstimate, ZillowException



class Address(models.Model):
	street_address = models.CharField(max_length=100)
	city_state_zip = models.CharField("City, State, Zip", max_length=200)
	#def __init__(self, address, citystatezip):
		#self.street_adress = address
		#self.cits_state_zip = citystatezip

	def assessedValue(self):
		try:
			return zEstimate(self.street_address, self.city_state_zip)
		except ZillowException as e:
			raise AssesmentException(e.message)

class AmountOwedFromUser(models.Model):
	amount_owed = models.FloatField()
	address = models.ForeignKey(Address)
	date_time_collected = models.DateTimeField()

class AssesmentException(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)
