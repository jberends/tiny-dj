from django.apps import AppConfig


class ShortUrlConfig(AppConfig):
    name = 'shorturl'

    def ready(self):
        pass
