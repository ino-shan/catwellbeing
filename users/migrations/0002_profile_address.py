# Generated by Django 2.2.5 on 2020-03-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='none', max_length=1024),
        ),
    ]
