# Generated by Django 3.2.7 on 2022-01-29 06:28

from django.db import migrations, models
import tick.utils


class Migration(migrations.Migration):

    dependencies = [
        ('tick', '0012_alter_ticket_identical'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='identical',
            field=models.IntegerField(default=tick.utils.create_new_number, editable=False, unique=True),
        ),
    ]
