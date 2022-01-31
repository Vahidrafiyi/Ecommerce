from django.apps import AppConfig


class EventLogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'event_log'

    def ready(self):
        import event_log.signals