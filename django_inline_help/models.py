from django.db import models
from django.utils.translation import ugettext_lazy as _


PLACEMENT_CHOISES = (
    ('top', _('Top')),
    ('left', _('Left')),
    ('right', _('Right')),
    ('bottom', _('Bottom')),
    ('', _('Auto')),
)


class Tooltip(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'), unique=True)

    is_activated = models.BooleanField(verbose_name=_('Is activated'))

    header = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Header'))
    text = models.TextField(null=True, verbose_name=_('Text'))
    placement = models.CharField(max_length=6, choices=PLACEMENT_CHOISES, verbose_name=_('Placement'), blank=True)

    class Meta:
        verbose_name = _('Tooltip')
        verbose_name_plural = _('Tooltips')

    def __str__(self):
        return self.name

    def __bool__(self):
        return bool(self.is_activated and self.text)
