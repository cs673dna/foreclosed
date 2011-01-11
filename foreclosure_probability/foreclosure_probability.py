from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms
from foreclosed.models import Address, AssesmentError, AmountOwedFromUser
import foreclosure_algorithm
from datetime import date


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

	form_street_address = form.cleaned_data['street_address']
	form_city_state_zip = form.cleaned_data['city_state_zip']
	form_amount_owed = form.cleaned_data['amount_owed']

	try:
		mortgage_address = Address.objects.get(
					street_address=form_street_address,
					city_state_zip=form_city_state_zip
					)
	except Address.DoesNotExist as e:
		mortgage_address = Address(
				street_address=form_street_address,
				city_state_zip=form_city_state_zip
				)
		mortgage_address.save()

	record_for_lead_gen = AmountOwedFromUser(
				amount_owed = form_amount_owed,
				address = mortgage_address,
				date_collected = date.today()
				)

	record_for_lead_gen.save()
				

	try:
		assessed_value = mortgage_address.assessed_value()
	except AssesmentError as e:
		return render_to_response(
			'failed_assesment_lookup.html',
			{'street_address': form_street_address,
			 'city_state_zip': form_city_state_zip,
			 'assesment_error': e.value}
		)
			
	future_values = foreclosure_algorithm.future_values(
						assessed_value, 
						2010, 
						10)
	
	return_values = foreclosure_algorithm.foreclosure_probability(
		assessed_value, 
		form_amount_owed)
	
	return render_to_response(
		'foreclosure_probability_result.html',
		{'probability': return_values[0], 
		'algorithm_message': return_values[1],
		'zestimate': assessed_value,
		'future_values': future_values})
