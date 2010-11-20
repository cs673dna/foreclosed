from django import forms

class HAMPForm(forms.Form):
	numberOfUnits = forms.CharField(label="Number of Units")
	freddiFannie = forms.BooleanField(label="Mortage held by Freddie Mac or Fannie May?")
