from django import forms
from address import Address
from hamp_algorithm import meetsModificationRequirements
from mortgage import Mortgage
from django.shortcuts import render_to_response
from django.template import RequestContext

class HAMPForm(forms.Form):
	
	firstMortgage = forms.BooleanField(label = 
		"Is this the first mortgage on the property")

	ownerOccupied = forms.BooleanField(label = "Is the property owner-occupied")
	
	current = forms.BooleanField(label = "Is the mortgage current?")

	freddiFannie = forms.BooleanField(
		label = "Mortage held by Freddie Mac or Fannie May?")

	monthlyPayment = forms.DecimalField( label = "Monthly Mortgage Payment",
		decimal_places = 2,
		min_value = 0)

	amountOwed = forms.DecimalField( label = "Amount owed on mortgage",
		decimal_places = 2,
		min_value = 0)

	numberOfUnits = forms.CharField(label = "Number of Units")

	streetAddress = forms.CharField(label = "Address")
	cityStateZip = forms.CharField(label = "City, State, Zip")

	monthlyIncome = forms.DecimalField(label="Monthly Income",
		decimal_places = 2,
		min_value = 0)


def HAMP(request):
	if request.method == 'POST':
		form = HAMPForm(request.POST)
		if form.is_valid():

			mortgage_address = Address(form.cleaned_data['streetAddress'],
				form.cleaned_data['cityStateZip'])

			#Mortgage
			amountOwed = form.cleaned_data['amountOwed']
			units = form.cleaned_data['numberOfUnits']
			ownerOccupied = form.cleaned_data['ownerOccupied']
			monthlyPayment = form.cleaned_data['monthlyPayment']
			first = form.cleaned_data['firstMortgage']
			current = form.cleaned_data['current']

			mortgage = Mortgage(monthlyPayment,
				amountOwed,
				first,
				ownerOccupied,
				units,
				current)

			#User's Financial Situation
			monthlyIncome = form.cleaned_data['monthlyIncome']
			
			hampTry = meetsModificationRequirements(monthlyIncome, mortgage, mortgage_address)

			if hampTry[0]:
				modificationMessage = True
			else:
				modificationMessage = hampTry[1]


			try:
				assessed_message = mortgage_address.assessedValue()
			except ZillowException as e:
				assessed_message = e

			return render_to_response('hamp_results.html', 
				{'modify': modificationMessage,
				'zestimate': assessed_message})

	else:
		form = HAMPForm()
		
	return render_to_response('HAMP.html', {'form': form}, context_instance=RequestContext(request))
