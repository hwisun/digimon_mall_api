# Generated by Django 2.2.4 on 2019-08-09 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monster', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermonster',
            old_name='tiems',
            new_name='times',
        ),
    ]
