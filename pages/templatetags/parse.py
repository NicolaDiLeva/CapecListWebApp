from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='parse')
@stringfilter

def parse(value, arg):
    
    parsed = []
    split = value.split("::")
    
    for s in split:
        if s=='':
            pass
        else:
            replace = s.replace(':', ' ')
            parsed.append(replace)
    
    return parsed