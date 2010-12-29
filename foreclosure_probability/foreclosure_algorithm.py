import math
HOME_PRICE_INFLATION_RATE = 0.034

def calc_foreclosure_probability(assessed_value, amountOwed):
	if not hasNegativeEquity(assessed_value, amountOwed): 
		return 0, "You do not have negative equity, \
			there is no probability of forecosure\
			if you sell your house."
	
	negativeEquity = amountOwed - assessed_value
	percentOfNegativeEquity = negativeEquity / assessed_value
	return	percentValueOfForeclosure(percentOfNegativeEquity)

def percentValueOfForeclosure(percentOfNegEq):
	if percentofNegEq > 1:
		return 1
	else:
		return 1 * percentOfNegEq


def hasNegativeEquity(assessed_value, amountOwed):
	if amountOwed > assessed_value:
		return True
	else:	
		return False

def future_values(present_value, start_year, years):
	return [[str(year), present_value * math.pow(( 1.0 + HOME_PRICE_INFLATION_RATE ), (year - start_year))] for year in range(start_year, start_year + years)]



