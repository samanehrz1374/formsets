# Generated by Django 4.0.3 on 2022-03-15 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsets', '0012_rename_programmer_language_skills'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Language',
            new_name='skillsModel',
        ),
    ]
