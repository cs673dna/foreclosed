from zillow import zEstimate
from django.db import models

class old_Address(models.Model):
	street_address = models.CharField(max_length=100)
	city_state_zip = models.CharField("City, State, Zip", max_length=200)
	#def __init__(self, address, citystatezip):
		#self.street_adress = address
		#self.cits_state_zip = citystatezip

	def assessedValue(self):
		return zEstimate(self.street_address, self.city_state_zip)
