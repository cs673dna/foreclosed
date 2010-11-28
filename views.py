from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from hamp import HAMPForm, HAMP
from django.shortcuts import render_to_response

def index(request):
	t = loader.get_template('index.html')
	c = Context()

	return HttpResponse(t.render(c))
