# Generated by Django 5.0.1 on 2024-01-08 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0003_alter_studentdetails_sdept'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdetails',
            name='sfees',
        ),
    ]
