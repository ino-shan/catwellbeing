# Generated by Django 2.2.5 on 2020-03-26 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=8)),
                ('cat_weight', models.FloatField()),
                ('cat_weight_unit', models.CharField(max_length=16)),
                ('cat_breed_list', models.CharField(max_length=64)),
                ('Spayed_Neutred', models.CharField(max_length=32)),
                ('microchip_number', models.CharField(max_length=64)),
                ('insurance_provider_list', models.CharField(max_length=64)),
                ('insurance_policy_number', models.CharField(max_length=64)),
                ('clinic_name', models.CharField(max_length=64)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder_type', models.CharField(max_length=128)),
                ('reminder_date', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reminder_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cat')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('description', models.CharField(max_length=2048)),
                ('imagename', models.CharField(max_length=1024)),
                ('imageurl', models.CharField(max_length=1024)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cat')),
            ],
        ),
    ]