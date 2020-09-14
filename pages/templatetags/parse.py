from django import template
from django.template.defaultfilters import stringfilter
import re


register = template.Library()

@register.filter(name='parse')
@stringfilter

def parse(value, arg):
    
    replace1 = value.replace('::',';')
    replace2 = replace1.replace(':', ' ')
    strip = replace2.lstrip(';')
    parsed = strip.replace(';', '\n')
    
    return parsed