# Generated by Django 2.2.11 on 2020-05-03 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20200503_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=8),
        ),
    ]
