from __future__ import division
from math import log, pow
HOME_PRICE_INFLATION_RATE = 0.034

probability_curve = ((-5, 0), (-4, 0), (-4, 0), (-3, 0), (-2, 0), (-1, .01),
		     (0, .04), (1, .10), (2, .14), (3, .18), 
		     (4, .2), (5, .20), (10000, .20))

def foreclosure_probability(assessed_value, amount_owed):
	assessed_value = float(assessed_value)
	amount_owed = float(amount_owed)
	loan_to_value = amount_owed / assessed_value
	log_loan_to_value = log(loan_to_value) 
	for point in probability_curve:
		if point[0] > log_loan_to_value:
			probability = point[1]

	
	return probability, None


def future_values(present_value, start_year, years):
	return [[str(year), present_value * pow(( 1.0 + HOME_PRICE_INFLATION_RATE ), (year - start_year))] for year in range(start_year, start_year + years)]
