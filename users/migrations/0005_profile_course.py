# Generated by Django 3.2.7 on 2022-01-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('users', '0004_profile_online_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='course',
            field=models.ManyToManyField(to='course.Course'),
        ),
    ]
