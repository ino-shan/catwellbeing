# Generated by Django 2.2.11 on 2020-05-03 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20200503_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='cat_breed_list',
            new_name='cat_breed',
        ),
        migrations.RenameField(
            model_name='cat',
            old_name='insurance_provider_list',
            new_name='insurance_provider',
        ),
    ]
