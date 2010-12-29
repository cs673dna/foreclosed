from decimal import Decimal

from foreclosed.models import AssesmentException

PAYMENT_TO_INCOME_GUIDELINE = Decimal(".31")
MAX_MODIFICATION_AMOUNT = 729750
MAX_UNITS = 5


def meetsModificationRequirements(monthlyIncome, mortgage, address):

	if monthlyIncome * PAYMENT_TO_INCOME_GUIDELINE > mortgage.monthlyPayment:
		return False, "Monthly Income too high \
			relative to mortgage payment for HAMP modification."

	if not mortgage.ownerOccupied:
		return False, "Mortgage must be on an owner-occupied house"

	if mortgage.units > MAX_UNITS:
		return False, ("mortgage must be on a house with less than %s \
			units for HAMP modification. \
			Your mortgage has %s units" % 
			(MAX_UNITS, mortgage.units))

	if not mortgage.first:
		return False, "Only first mortgages can be modified with HAMP."

	try:
		return mortgageMeetsHAMPRequirements(mortgage, address) 
	except AssesmentException as e:
		return False, e.message	


def mortgageMeetsHAMPRequirements(mortgage, address):
	if mortgage.amountOwed > address.assessedValue():
		return False, "Amount owed must be less than \
			assessed value for HAMP modifiaction."

	if mortgage.amountOwed > MAX_MODIFICATION_AMOUNT:
		return False, ("Amount owed must be less than %s" 
			% (MAX_MODIFICATION_AMOUNT))

	if not mortgage.current:
		return False, "You must be current on \
			your mortgage to recieve HAMP modification."

	return True,


class HampAlgorithmException(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)	
