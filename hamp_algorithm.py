
PAYMENT_TO_INCOME_GUIDELINE = .31
MAX_MODIFICATION_AMOUNT = 729750
MAX_UNITS = 5

class HAMPAlgorithm():
	def __init__(self):
		pass

	def meetsModificationRequirements(financialPicture, mortage, address):
	
		if not finacialPicture.monthlyIncome * PAYMENT_TO_INCOME_GUIDELINE > mortage.monthlyPayment:
			return False, "Monthly Income too high relative to mortage payment for HAMP modification."

		if not (mortage.OwnerOccupied and mortage.units < MAX_UNITS):
			return False, "Mortage must be on an owner occupied \
				house with less than %s unis for HAMP modification." % (MAX_UNITS)

		if not mortage.first:
			return False, "Only first mortages can be modified with HAMP."

		return mortageMeetsHAMPRequirements(mortage, address) 


	def mortageMeetsHAMPRequirements(mortage, address):
		if not mortage.amountowed > address.AssessedValue:
			return False, "Amount owed must be less than assessed value for HAMP modifiaction."

		if not mortage.amountowed <= MAX_MODIFICATION_AMOUNT:
			return False, "Amount owed must be less than %s" % (MAX_MODIFICATION_AMOUNT)

		if not mortage.current:
			return False, "You must be current on your mortage to recieve HAMP modification."

		return True
