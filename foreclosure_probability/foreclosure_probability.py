from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms
from foreclosed.models import Address
import foreclosure_algorithm

class ForeclosureProbabilityForm(forms.Form):

	amount_owed = forms.FloatField(label="Amount Owed")
	street_address = forms.CharField(label="Address")
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


def _process_form(form):
	mortgage_address = Address(
		form.cleaned_data['street_address'],
		form.cleaned_data['city_state_zip'])

	amount_owed = form.cleaned_data['amount_owed']

	assessed_value = mortgage_address.assessed_value()

	future_values = foreclosure_algorithm.future_values(assessed_value, 2010, 10)
	
	return_values = foreclosure_algorithm.calc_foreclosure_probability(
		assessed_value, 
		amount_owed)
	
	return render_to_response(
		'foreclosure_probability_result.html',
		{'probability': return_values[0], 
		'algorithm_message': return_values[1],
		'zestimate': assessed_value,
		'future_values': future_values})
