# Generated by Django 3.1.12 on 2022-01-03 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='no_of_days',
            field=models.PositiveIntegerField(),
        ),
    ]
