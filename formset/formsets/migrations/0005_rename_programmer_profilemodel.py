# Generated by Django 4.0.3 on 2022-03-15 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsets', '0004_programmer_language'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Programmer',
            new_name='ProfileModel',
        ),
    ]
