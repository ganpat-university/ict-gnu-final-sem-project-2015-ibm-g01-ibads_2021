# Generated by Django 3.2.8 on 2022-03-16 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serious_squad_app', '0012_auto_20220316_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='visibility',
        ),
        migrations.AlterField(
            model_name='data',
            name='specific_user',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]