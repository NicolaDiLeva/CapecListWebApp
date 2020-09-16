from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()

@register.filter(name='int_parse')
@stringfilter

def int_parse(value, arg):	
	v = [int(s) for s in re.findall(r'\b\d+\b', value)]
	if len(v)!=0:
		return v[0]
	return None