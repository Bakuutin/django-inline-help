from copy import deepcopy

from django.conf import settings
from django.template.loader import render_to_string

DEFAULT_SETTINGS = {
    'DEFAULTS': {
        'placement': 'top',
        'text': None,
        'is_activated': True,
    },
    'JS': {  # http://getbootstrap.com/javascript/#popovers-options
        'animation': True,
        'delay': 0,
        'html': True,
        'selector': False,
        'template': render_to_string('django_inline_help/tooltip.html').replace('\n', ''),
        'trigger': 'hover focus',
    }
}

SETTINGS = deepcopy(DEFAULT_SETTINGS)
for key, value in getattr(settings, 'INLINE_HELP', {}).items():
    SETTINGS[key].update(value)


DEFAULTS = SETTINGS['DEFAULTS']
JS = SETTINGS['JS']
