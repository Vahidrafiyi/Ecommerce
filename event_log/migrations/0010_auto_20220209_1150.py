# Generated by Django 3.2.7 on 2022-02-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_log', '0009_rename_loguserinfo_loguseractivity'),
    ]

    operations = [
        migrations.AddField(
            model_name='loguseractivity',
            name='browser',
            field=models.CharField(default='chrome', max_length=100),
        ),
        migrations.AddField(
            model_name='loguseractivity',
            name='device',
            field=models.CharField(default='pc', max_length=100),
        ),
    ]