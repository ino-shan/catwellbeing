# Generated by Django 2.2.11 on 2020-05-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_veterinary_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='veterinary',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]
