from django.urls import path
from event_log.models import LogUserActivity
from event_log.views import LogUserAPI
urlpatterns = [
    path('all_log', LogUserAPI.as_view()),
]