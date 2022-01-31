from django.db import models
from django.contrib.auth.models import User

class LogUserInfo(models.Model):
    LOG_ACTIONS = (
        ('login', 'User logged in'),
        ('delete_object', 'User delete object'),
        ('create_object', 'User create object'),
        ('buy_object', 'User buy object'),
        #   ...     ...     ...
        # Whatever you need here
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    action = models.CharField(max_length=20, default='login', choices=LOG_ACTIONS, verbose_name= 'action')
    date = models.DateTimeField(auto_now_add=True, verbose_name='date')
    ip = models.GenericIPAddressField()

    class Meta:
        ordering = ['-date']
        verbose_name = 'Action log'
        verbose_name_plural = 'Actions log'
