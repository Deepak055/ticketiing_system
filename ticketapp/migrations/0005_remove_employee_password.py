# Generated by Django 2.2.20 on 2021-05-06 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0004_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='password',
        ),
    ]