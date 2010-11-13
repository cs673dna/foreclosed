from django.http import HttpResponse
from django.template import Context, loader
#from HAMP import HAMPForm


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
	t = loader.get_template('HAMP_RESULT.html')
	c = Context()
	
	return HttpResponse(t.render(c))
