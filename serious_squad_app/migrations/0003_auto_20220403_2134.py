# Generated by Django 3.2.8 on 2022-04-03 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serious_squad_app', '0002_useractivity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useractivity',
            old_name='requested_at',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='useractivity',
            old_name='requested_at_1',
            new_name='time_1',
        ),
    ]