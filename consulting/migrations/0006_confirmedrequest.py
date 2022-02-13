# Generated by Django 3.2.7 on 2022-02-13 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0005_auto_20220212_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmedRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.BigIntegerField()),
                ('response', models.TextField()),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulting.consultationform')),
            ],
        ),
    ]