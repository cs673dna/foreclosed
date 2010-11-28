class ProbabilityAlgorithm():
	def __init__(self):
		pass

	def hasNegativeEquity(assessedValue, amountOwed):
		if amountOwed > assessedValue:
			return True
		else:	
			return False
	
	def probabilityOfForeclosure (assessedValue, amountOwed):
		if not hasNegativeEquity(assessedValue, amountOwed): 
			return 0, "You do not have negative equity, \
				there is not probability of forecosure\
				if you sell your house."
		
		negativeEquity = amountOwed - assessedValue
		percentOfNegativeEquity = negativeEquity / assessedValue
		return	percentValueOfForeclosure(percentOfNegativeEquity)

	def percentValueOfForeclosure(percentOfNegEq):
		if percentofNegEq > 1:
			return 1
		else:
			return 1 * percentOfNegEq
