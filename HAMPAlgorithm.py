
PAYMENT_TO_INCOME_GUIDELINE = .31

class HAMPAlgorithm():
	def __init__(self):
		pass

	def meetsModificationRequirements(financialPicture, mortage, address):
	
		if mortageMeetsHAMPRequirements(mortage, address) 
		and 
		finacialPicture.monthlyIncome * PAYMENT_TO_INCOME_GUIDELINE > mortage.monthlyPayment:
			return True
		else:
			return False


	def mortageMeetsHAMPRequirements(mortage, address):
		if 
