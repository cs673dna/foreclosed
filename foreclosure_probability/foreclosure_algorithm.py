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

def future_values(present_value, start_year, years):
	return [(year, present_value * math.pow(( 1.0 + HOME_PRICE_INFLATION_RATE ), (year - start_year))) for year in range(start_year, start_year + years)]
