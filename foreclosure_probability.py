class ProbabilityAlgorithm():
	
	def probabilityOfForeclosure (request):
		if not hasNegativeEquity(assessedValue, amountOwed): 
			return 0, "You do not have negative equity, \
				there is no probability of forecosure\
				if you sell your house."
		
		negativeEquity = amountOwed - assessedValue
		percentOfNegativeEquity = negativeEquity / assessedValue
		return	percentValueOfForeclosure(percentOfNegativeEquity)

	def percentValueOfForeclosure(percentOfNegEq):
		if percentofNegEq > 1:
			return 1
		else:
			return 1 * percentOfNegEq


	def hasNegativeEquity(assessedValue, amountOwed):
		if amountOwed > assessedValue:
			return True
		else:	
			return False
