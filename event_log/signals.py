import user_agents.parsers
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from event_log.models import LogUserActivity
from user_agents import parse
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ua_string = request.META.get('HTTP_USER_AGENT')
    user_agent = parse(ua_string)
    LogUserActivity.objects.create(user=request.user.get_username(), ip=request.META.get('REMOTE_ADDR'), user_agent=str(user_agent))

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    ua_string = request.META.get('HTTP_USER_AGENT')
    user_agent = parse(ua_string)
    LogUserActivity.objects.create(user=request.user.get_username(), ip=request.META.get('REMOTE_ADDR'), action=LogUserActivity.LOG_ACTIONS[4][0], user_agent=str(user_agent))
@receiver(user_login_failed)
def log_user_failed_login(sender, credentials, request, **kwargs):
    ua_string = request.META.get('HTTP_USER_AGENT')
    user_agent = parse(ua_string)
    LogUserActivity.objects.create(user=credentials['username'], ip=request.META.get('REMOTE_ADDR'), action=LogUserActivity.LOG_ACTIONS[6][0], user_agent=str(user_agent))

from django.contrib.admin.models import LogEntry