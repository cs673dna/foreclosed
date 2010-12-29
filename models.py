from django.template import RequestContext
from django.db import models
from address.zillow import zEstimate, ZillowException
from django.forms import ModelForm
from django.shortcuts import render_to_response

class Address(models.Model):
	street_address = models.CharField(max_length=100)
	city_state_zip = models.CharField("City, State, Zip", max_length=200)
	#def __init__(self, address, citystatezip):
		#self.street_adress = address
		#self.cits_state_zip = citystatezip

	def assessed_value(self):
		try:
			return zEstimate(self.street_address, self.city_state_zip)
		except ZillowException as e:
			raise AssesmentException(e.message)

class AmountOwedFromUser(models.Model):
	amount_owed = models.FloatField()
	address = models.ForeignKey(Address)
	date_time_collected = models.DateTimeField()

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

class AssesmentException(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)
