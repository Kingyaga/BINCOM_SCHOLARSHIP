from django import template

register = template.Library()

@register.filter(name='instanceof')
def instanceof(value):
    return value.__class__.__name__