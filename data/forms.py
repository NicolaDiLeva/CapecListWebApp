from django import forms

class IdForm(forms.Form):
	id = forms.IntegerField()