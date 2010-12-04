import math
HOME_PRICE_INFLATION_RATE = 0.034

def calc_foreclosure_probability(assessedValue, amountOwed):
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

def future_value(present_value, years):
	return [present_value * math.pow((1 + HOME_PRICE_INFLATION_RATE), year) for year in range(1, years)]
