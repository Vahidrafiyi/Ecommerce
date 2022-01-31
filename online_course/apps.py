from django.apps import AppConfig


class OnlineCourseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'online_course'

    def ready(self):
        import online_course.signals
