from django.template import Library
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import re

register = Library()
# https://stackoverflow.com/questions/721035/django-templates-stripping-spaces
@stringfilter
def spacify(value, autoescape=None):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    return mark_safe(re.sub('\s', '&'+'nbsp;', esc(value)))
spacify.needs_autoescape = True
register.filter(spacify)

# https://stackoverflow.com/questions/34571880/how-to-check-in-template-if-user-belongs-to-a-group
@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 