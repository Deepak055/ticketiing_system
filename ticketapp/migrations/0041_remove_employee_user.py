# Generated by Django 2.2.20 on 2021-05-09 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0040_auto_20210509_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
    ]
