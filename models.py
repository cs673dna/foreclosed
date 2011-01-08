from django.template import RequestContext
from django.db import models
from address.zillow import zEstimate, ZillowError
from django.forms import ModelForm
from django.shortcuts import render_to_response

class Address(models.Model):
	street_address = models.CharField("Address", max_length=100)
	city_state_zip = models.CharField("City, State, Zip", 
						max_length=200)

	class Meta:
		unique_together = ("street_address", "city_state_zip")

	def assessed_value(self):
		try:
			return zEstimate(self.street_address, 
					self.city_state_zip)
		except ZillowError as e:
			raise AssesmentError(e.value)

class AmountOwedFromUser(models.Model):
	amount_owed = models.FloatField()
	address = models.ForeignKey(Address)
	date_collected = models.DateTimeField()

class HAMPModification(models.Model):
	amount_owed = models.FloatField()
	address = models.OneToOneField(Address)

class HAMPModificationForm(ModelForm):
	class Meta:
		model = HAMPModification


def HAMP_new(request):
	if request.method == 'POST':
		form = HAMPModificationForm(request.POST)
		h = form.save()

	form = HAMPModificationForm()

	return render_to_response('HAMP_new.html',
		{'form': form},
		context_instance=RequestContext(request))

class AssesmentError(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)
