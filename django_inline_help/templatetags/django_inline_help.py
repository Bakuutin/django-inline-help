import json

from django import template

from ..models import Tooltip
from .. import settings

register = template.Library()


@register.inclusion_tag('django_inline_help/button.html')
def inline_help(name):
    tooltip, _ = Tooltip.objects.get_or_create(name=name, defaults=settings.DEFAULTS)
    return {'tooltip': tooltip}


@register.inclusion_tag('django_inline_help/scripts.html')
def init_inline_help():
    return {'options': json.dumps(settings.JS)}
