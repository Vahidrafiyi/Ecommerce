# Generated by Django 4.0.2 on 2022-02-08 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_log', '0002_alter_loguserinfo_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loguserinfo',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]