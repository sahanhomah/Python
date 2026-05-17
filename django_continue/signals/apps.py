from django.apps import AppConfig


class SignalsConfig(AppConfig):
    name = 'signals'


    def ready(self):
        from . import signals
