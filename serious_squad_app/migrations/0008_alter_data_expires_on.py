# Generated by Django 3.2.8 on 2022-02-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serious_squad_app', '0007_data_expires_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='expires_on',
            field=models.DateField(null=True),
        ),
    ]