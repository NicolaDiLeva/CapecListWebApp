import django_filters
from data.models import *

class DataFilter(django_filters.FilterSet):
	class Meta:
		model = DomainsOfAttack
		fields = ['id']