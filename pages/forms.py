from django import forms
from data.models import *

class HomeForm(forms.ModelForm):
	class Meta:
		model = DomainsOfAttack
		fields = ['id']