from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from tick.models import Ticket, TicketMessage
@receiver(post_save, sender=Ticket)
def create_update_ticket(sender, instance, **kwargs):
     if instance:
          TicketMessage.objects.create(message='Type SomeThing', ticket_id=instance)

