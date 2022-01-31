from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from online_course.models import Episode


import os
@receiver(post_save, sender=Episode)
def create_instance(sender, instance, created, **kwargs):
    if created:
        os.mkdir(f'files/{instance.episode_title}')
