# Generated by Django 2.2.11 on 2020-05-01 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veterinary',
            name='rating',
        ),
    ]
