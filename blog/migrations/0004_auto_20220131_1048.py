# Generated by Django 3.2.7 on 2022-01-31 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220131_1007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',)},
        ),
        migrations.AlterField(
            model_name='article',
            name='article_alt',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
