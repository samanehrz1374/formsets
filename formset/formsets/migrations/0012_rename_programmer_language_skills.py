# Generated by Django 4.0.3 on 2022-03-15 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsets', '0011_profilemodel_language'),
    ]

    operations = [
        migrations.RenameField(
            model_name='language',
            old_name='programmer',
            new_name='skills',
        ),
    ]