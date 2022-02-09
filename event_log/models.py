import pytz
from django.db import models
from django.contrib.auth.models import User
import datetime
from django_jalali.db import models as jmodels
class LogUserActivity(models.Model):
    LOG_ACTIONS = [
        ('logged in', 'logged in'),
        ('delete something', 'delete something'),
        ('create something', 'create something'),
        ('buy something', 'buy something'),
        ('logged out', 'logged out'),
        ('signed up', 'signed up'),
        ('failed to log in', 'failed to log in')
        #   ...     ...     ...
        # Whatever you need here
    ]
    user = models.CharField(max_length=100)
    action = models.CharField(max_length=20, default=LOG_ACTIONS[0][0], choices=LOG_ACTIONS, verbose_name= 'action')
    date = jmodels.jDateTimeField(auto_now_add=True)
    browser = models.CharField(max_length=100, default='chrome')
    device = models.CharField(max_length=100, default='pc')
    os = models.CharField(max_length=100, default='windows')
    ip = models.GenericIPAddressField()

    class Meta:
        ordering = ['-date']
        verbose_name = 'Action log'
        verbose_name_plural = 'Actions log'

    def __str__(self):
        return self.user + ' ' + self.action + ' / ' + str(self.date)[:19]
