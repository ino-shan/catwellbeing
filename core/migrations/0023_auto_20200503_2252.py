# Generated by Django 2.2.11 on 2020-05-03 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20200503_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='cat_weight_unit',
            field=models.CharField(choices=[('kg', 'kg'), ('lb', 'lb')], max_length=16),
        ),
    ]