from zillow import zEstimate

class Address():
	def __init__(self, address, citystatezip):
		self.address = address
		self.citystatezip = citystatezip


	def assessedValue(self):
		return zEstimate(self.address, self.citystatezip)
