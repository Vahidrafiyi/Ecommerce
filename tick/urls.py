from django.urls import path
from tick.views import GetAllTicket, CustomTicket, SendTicket, GetAllTicketMessage, CustomTicketMessage, SendTicketMessage
urlpatterns = [
    # API for Tickets
    path('all_ticket/', GetAllTicket.as_view()),
    path('custom_ticket/<int:pk>', CustomTicket.as_view()),
    path('send_ticket', SendTicket.as_view()),
    # API for Ticket Messages
    path('all_message/', GetAllTicketMessage.as_view()),
    path('custom_message/<int:pk>', CustomTicketMessage.as_view()),
    path('send_message', SendTicketMessage.as_view()),
    ]