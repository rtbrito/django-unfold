from django.apps import AppConfig
from django.conf import settings


class ConstanceConfig(AppConfig):
    name = "unfold.contrib.constance"
    label = "unfold_constance"

    def ready(self):
        try:
            from .settings import ADDITIONAL_FIELDS

            settings.CONSTANCE_ADDITIONAL_FIELDS = ADDITIONAL_FIELDS
        except ImportError:
            import logging

            logging.error("Could not import ADDITIONAL_FIELDS from settings")
        return super().ready()
