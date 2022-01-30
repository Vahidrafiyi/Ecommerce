# Generated by Django 3.2.7 on 2022-01-18 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_course', '0002_auto_20220118_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinecourse',
            name='online_course_status',
            field=models.CharField(choices=[('pre-registration', 'Pre Registration'), ('running', 'Running'), ('done', 'Done')], default='running', max_length=100),
        ),
    ]
