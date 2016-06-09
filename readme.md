# Django Inline Help

A tool for creating editable tooltips.

### Installation:

0. `pip install git+https://github.com/Bakuutin/django-inline-help@v0.0.1`
1. Add `'django_inline_help'` to `INSTALLED_APPS`
2. `python manage.py migrate django_inline_help`

### Adding tooltip buttons to template:

1. To the list of scripts add `{% init_inline_help %}`
2. Add new tooltip button via `{% inline_help "Hello world!" %}`
3. Refresh the page
4. Set tooltip text from the admin site
5. Refresh the page again
