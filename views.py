from django.http import HttpResponse
from django.template import Context, loader


def hello(request):
	return HttpResponse("Hello World")

def index(request):
	t = loader.get_template('index.html')
	c = Context()

	return HttpResponse (t.render(c))
