from django.shortcuts import render_to_response, get_list_or_404
from django.template import RequestContext
from foreclosed.models import Address


def lead_gen_display(request):
	addresses = get_list_or_404(Address)
	return render_to_response(
	'lead_gen_table.html',
	{'addresses': addresses},
	context_instance = RequestContext(request))
