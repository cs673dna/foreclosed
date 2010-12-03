from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms

class ForeclosureProbabilityForm(forms.Form):

	amount_owed = forms.DecimalField(label="Amount Owed")
	steet_address = forms.CharField(label="Address")
	city_state_zip = forms.CharField(label="City, State, Zip")	
	

def foreclosure_probability(request):
	if request.method == 'POST':
		form = ForeclosureProbabilityForm(request.POST)	
		if form.is_valid():
			return _process_form(form)
	else:
		form = ForeclosureProbabilityForm()
		
	return render_to_response(
		'foreclosure_probability_entry.html', 
		{'form': form}, 
		context_instance = RequestContext(request))


def _process_form(request):
	mortgageAddress = Address(form.cleaned_data['street_address'],
		form.cleaned_data['city_state_zip'])

	amount_owed = form.cleaned_data['amount_owed']

	return_values = calc_foreclosure_probability(mortgageAddress.assessedValue(), 
		amount_owed)
	
	return render_to_response('foreclose_probability_result.html',
		{'probability': return_values[0], 
			'algorithm_message': return_values[1]})
	

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
