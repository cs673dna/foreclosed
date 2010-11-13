from django import forms

class HAMPForm(forms.Form):
	numberOfUnits = forms.CharField()
	freddiFannie = forms.RadioSelect()
