# Generated by Django 2.2.20 on 2021-05-07 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0008_remove_employee_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Employee_email',
        ),
    ]
