# Generated by Django 2.2.11 on 2020-05-04 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_auto_20200505_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='cat_photo',
            field=models.ImageField(blank=True, null=True, upload_to='catphotos/%Y/%m/%d'),
        ),
    ]