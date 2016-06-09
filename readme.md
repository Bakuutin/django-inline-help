# Django Inline Help

A tool for creating editable tooltips.

### Installation:

0. `pip install git+https://github.com/Bakuutin/django-inline-help@v0.0.1`
1. Add `'django_inline_help'` to `INSTALLED_APPS`
2. `python manage.py migrate django_inline_help`

### Adding tooltip buttons to the template:

0. At the top of the template put `{% load django_inline_help %}`
1. To the list of scripts add `{% init_inline_help %}`
2. Add tooltip button via `{% inline_help "Hello world!" %}`
3. Refresh the page
4. Set tooltip text from the admin site
5. Refresh the page again

### Settings

Button appears when tooltip is activated and has any text. Set default text if you want them to appear immidiately as added to template.

    INLINE_HELP = {
        'DEFAULTS': {
            'placement': 'top',  # empty string for auto
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
