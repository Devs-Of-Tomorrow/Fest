from django import template

register = template.Library()

@register.filter(name='is_registered')
def is_registered(festival, participate):
    keys = participate.keys()
    for id in keys:
        if int(id) == festival.id:
            return True
    return False;