# Generated by Django 2.2.11 on 2020-05-08 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_welcome_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='isvet',
            field=models.BooleanField(default=False),
        ),
    ]
