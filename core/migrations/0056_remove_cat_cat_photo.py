# Generated by Django 2.2.12 on 2020-05-06 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_auto_20200506_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='cat_photo',
        ),
    ]