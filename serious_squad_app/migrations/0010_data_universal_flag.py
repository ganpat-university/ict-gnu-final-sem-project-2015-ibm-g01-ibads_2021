# Generated by Django 3.2.8 on 2022-03-01 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serious_squad_app', '0009_alter_data_expires_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='universal_flag',
            field=models.BooleanField(default=False),
        ),
    ]
