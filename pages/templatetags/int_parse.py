from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()

@register.filter(name='int_parse')
@stringfilter

def int_parse(value, arg):  

    split2 = value.rsplit(' ',1)

    return split2