# Generated by Django 2.2.20 on 2021-05-09 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0037_auto_20210509_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]