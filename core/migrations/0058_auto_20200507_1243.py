# Generated by Django 2.2.11 on 2020-05-07 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_auto_20200506_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalrecord',
            name='imagename',
            field=models.CharField(default='none', max_length=1000),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='imageurl',
            field=models.CharField(default='none', max_length=1000),
        ),
    ]
