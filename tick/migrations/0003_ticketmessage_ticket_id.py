# Generated by Django 3.2.7 on 2022-01-24 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tick', '0002_remove_ticketmessage_ticket_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketmessage',
            name='ticket_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tick.ticket'),
        ),
    ]
