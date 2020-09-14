from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='split')
@stringfilter

def split(value, arg):
	
	replace1 = value.replace("::",";")
	replace2 = replace1.replace(":", " ")
	strip = replace2.lstrip(";")
	
	parse = strip.replace(";", "\n")
	
	return parse