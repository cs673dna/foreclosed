from django import template
import locale

locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')
register = template.Library()

@register.filter
def currency(value):
	return locale.currency(value, grouping=True)
