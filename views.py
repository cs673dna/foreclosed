from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from hamp import HAMPForm, HampCheck
from django.shortcuts import render_to_response

def hello(request):
	return HttpResponse("Hello World")

def index(request):
	t = loader.get_template('index.html')
	c = Context()

	return HttpResponse(t.render(c))

#def HAMP(request):
	#t = loader.get_template('HAMP_FORM.html')
	#c = Context()
#
	#return HttpResponse(t.render(c))

def HAMP(request):
	if request.method == 'POST':
		form = HAMPForm(request.POST)
		if form.is_valid():
			hampCheck = HampCheck()
			#Address
			hampCheck.address = form.cleaned_data['streetAddress']
			hampCheck.citystatezip = form.cleaned_data['cityStateZip']

			#Mortgage
			hampCheck.amountOwed = form.cleaned_data['amountOwed']
			hampCheck.units = form.cleaned_data['numberOfUnits']
			hampCheck.ownerOccupied = form.cleaned_data['ownerOccupied']
			hampCheck.monthlyPayment = form.cleaned_data['monthlyPayment']
			hampCheck.first = form.cleaned_data['firstMortgage']

			#Users Financial Situation
			hampCheck.monthlyIncome = form.cleaned_data['monthlyIncome']

			return render_to_response('hamp_results.html', {'modify': hampCheck.modifiable()})

	else:
		form = HAMPForm()
		
	return render_to_response('HAMP.html', {'form': form}, context_instance=RequestContext(request))
