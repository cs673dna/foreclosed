from decimal import Decimal

PAYMENT_TO_INCOME_GUIDELINE = Decimal(.31)
MAX_MODIFICATION_AMOUNT = 729750
MAX_UNITS = 5


def meetsModificationRequirements(monthlyIncome, mortage, address):

	if monthlyIncome * PAYMENT_TO_INCOME_GUIDELINE > mortage.monthlyPayment:
		return False, "Monthly Income too high relative to mortage payment for HAMP modification."

	if not mortage.ownerOccupied:
		return False, "Mortgage must be on an owner-occupied house"

	if mortage.units > MAX_UNITS:
		return False, "Mortage must be on a house with less than %s units for HAMP modification." % (MAX_UNITS)

	if not mortage.first:
		return False, "Only first mortages can be modified with HAMP."

	return mortageMeetsHAMPRequirements(mortage, address) 


def mortgageMeetsHAMPRequirements(mortage, address):
	if mortage.amountOwed > address.assessedValue():
		return False, "Amount owed must be less than assessed value for HAMP modifiaction."

	if mortage.amountOwed > MAX_MODIFICATION_AMOUNT:
		return False, "Amount owed must be less than %s" % (MAX_MODIFICATION_AMOUNT)

	if not mortage.current:
		return False, "You must be current on your mortage to recieve HAMP modification."

	return True,
