from django.shortcuts import render_to_response, get_list_or_404
from django import template
from foreclosed.models import AmountOwedFromUser
import locale


def lead_gen_display(request):
	leads = get_list_or_404(AmountOwedFromUser)
	return render_to_response(
	'lead_gen_table.html',
	{'leads': leads},
	context_instance = template.RequestContext(request))
