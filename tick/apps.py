from django.apps import AppConfig


class TickConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tick'
    def ready(self):
        import tick.signals
