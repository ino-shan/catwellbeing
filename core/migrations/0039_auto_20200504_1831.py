# Generated by Django 2.2.11 on 2020-05-04 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20200504_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='Spayed_Neutred',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
