# Generated by Django 4.2.4 on 2023-08-08 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GeneralSettings',
            new_name='GeneralSetting',
        ),
    ]
