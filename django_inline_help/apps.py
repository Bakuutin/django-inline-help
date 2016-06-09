from django.apps.config import AppConfig
from django.utils.translation import ugettext_lazy as _


class InlineHelpConfig(AppConfig):
    name = 'django_inline_help'
    verbose_name = _('Tooltips')
