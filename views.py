from django.http import HttpResponse
from django.template import Context, loader
from hamp import HAMPForm
from django.shortcuts import render_to_response


def hello(request):
	return HttpResponse("Hello World")

def index(request):
	t = loader.get_template('index.html')
	c = Context()

	return HttpResponse(t.render(c))

def HAMP(request):
	t = loader.get_template('HAMP_FORM.html')
	c = Context()

	return HttpResponse(t.render(c))

def HAMPResults(request):
	if request.method == 'POST':
		form = HAMPForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thank you for submitting HAMP form/')

	else:
		form = HAMPForm()
		
	return render_to_response('HAMP.html', {'form': form})

def administrate(request):
	return render_to_response('base_Admin.html')
