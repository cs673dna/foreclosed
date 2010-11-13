from decimal import *

class ProbabilityAlgorithm():
	def __init__(self):
		pass

	def hasNegativeEquity(assessedValue, amountOwed):
		if amountOwed > assessedValue:
			return True
		else:	
			return False
	
	def probabilityOfForeclosure (assessedValue, amountOwed):
		if hasNegativeEquity(assessedValue, amountOwed) is False:
			return "there is no risk of foreclosure if you just sell your house"
		
		negativeEquity = Decimal(amountOwed) - Decimal(assessedValue)
		percentOfNegativeEquity = negativeEquity / assessedValue
		return	percentValueOfForeclosure(percentOfNegativeEquity)

	def percentValueOfForeclosure(percentOfNegEq):
		if percentofNegEq > 1.0:
			return 100
		else:
			return 100.0 * percentOfNegEq
