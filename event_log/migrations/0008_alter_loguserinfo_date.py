# Generated by Django 3.2.7 on 2022-02-09 07:44

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('event_log', '0007_remove_loguserinfo_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loguserinfo',
            name='date',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
    ]