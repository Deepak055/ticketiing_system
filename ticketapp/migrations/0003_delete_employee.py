# Generated by Django 2.2.20 on 2021-05-06 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0002_employee_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='employee',
        ),
    ]