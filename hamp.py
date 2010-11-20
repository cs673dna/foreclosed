from django import forms

class HAMPForm(forms.Form):
	numberOfUnits = forms.CharField(label="Number of Units", help_text="Number of units in the property whose mortage you would like to modify")
	freddiFannie = forms.BooleanField()
