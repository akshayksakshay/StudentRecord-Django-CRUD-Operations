# Generated by Django 5.0.1 on 2024-01-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0002_rename_teacher_marklist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='sdept',
            field=models.CharField(choices=[('CS', 'Computer Science'), ('BM', 'Bio Maths'), ('CM', 'Commerce'), ('HM', 'Humanities')], max_length=50),
        ),
    ]