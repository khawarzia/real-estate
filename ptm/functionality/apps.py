from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class FunctionalityConfig(AppConfig):
    name = 'functionality'
    verbose_name = _('functions')

    def ready(self):
        import functionality.signals
