from datetime import datetime
from ipware import get_client_ip
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from event_log.models import LogUserInfo


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    print('user {} logged in {}'.format(User.username, request.META.get('HTTP_REFERER')))
    print(datetime.now())
    ip, is_routable = get_client_ip(request)
    if ip is None:
        print("Unable to get the client's IP address")
    else:
        print(f"IP address is: {ip}")
        if is_routable:
            print("The client's IP address is publicly routable on the Internet")
        else:
            print("The client's IP address is private")
@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    print(f'user {User.username} logged out')
    print(datetime.now())

@receiver(user_login_failed)
def log_user_failed_login(sender, credentials, request, **kwargs):
    print(f'user {User.username} faild to logged in')
    print(datetime.now())