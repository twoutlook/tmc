
from django import template

register = template.Library()

@register.filter(is_safe=False)
def default_if_none_zero(value, arg):
    """If value is None, use given default."""
    # print(value)
    # if value:
    if value == 'None':
        return arg
    if value == None:
        return arg
    if value == 0:
        return arg

    return value