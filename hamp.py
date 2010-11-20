from django import forms
from address import Address
from hamp_algorithm import meetsModificationRequirements
from mortgage import Mortgage

class HAMPForm(forms.Form):
	
	firstMortgage = forms.BooleanField(label = 
		"Is this the first mortgage on the property")

	ownerOccupied = forms.BooleanField(label = "Is the property owner-occupied")

	freddiFannie = forms.BooleanField(
		label = "Mortage held by Freddie Mac or Fannie May?")

	monthlyPayment = forms.DecimalField( label = "Monthly Mortgage Payment",
		decimal_places = 2,
		min_value = 0)

	amountOwed = forms.DecimalField( label = "Amount owed on mortgage",
		decimal_places = 2,
		min_value = 0)

	numberOfUnits = forms.CharField(label = "Number of Units")

	streetAddress = forms.CharField(label = "Address")
	cityStateZip = forms.CharField(label = "City, State, Zip")


	monthlyIncome = forms.DecimalField(label="Monthly Income",
		decimal_places = 2,
		min_value = 0)

class HampCheck():
	def __init__(self):
		pass

	def modifiable(self):
		address = Address(self.address, self.citystatezip)		
		mortage = Mortgage(self.monthlyPayment, 
			self.amountOwed, 
			self.first,
			self.ownerOccupied,
			self.units)

		return meetsModificationRequirements(self.monthlyIncome, mortage, address)
