from django.template import RequestContext
from django.shortcuts import render_to_response

def foreclosureProbability (request):
	if request.method == 'POST':
		form = ForeclosureProbability(request.POST)	
		if form.is_valid():
			return processForm(form)

	else:
		form = ForeclosureProbability()
		
	return render_to_response('foreclosure_probability_entry.html', 
		{'form': form}, 
		context_instance = RequestContext(request))


def processForm(form):
	mortgageAddress = Address(form.cleaned_data['street_address'],
		form.cleaned_data['city_state_zip'])

	amountOwed = form.cleaned_data['amount_owed']

	return_values = foreclosureProbability(mortgageAddress.assessedValue(), 
		amountOwed)
	
	return render_to_response('foreclose_probability_result.html',
		{'probability': return_values[0], 
			'algorithm_message': return_values[1]})
	

def foreclosureProbability(assessedValue, amountOwed):
	
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

class ForeclosureProbability(forms.form):
	def __init__():
		pass	
