# Generated by Django 2.2.20 on 2021-05-09 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0041_remove_employee_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]
