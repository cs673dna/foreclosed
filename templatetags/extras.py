from django imoprt template
import locale

locale.setlocale(locale.LC_ALL, '')
register = template.Library()

@register.filter
def currency(value):
	return locale.currency(value, group=True)
