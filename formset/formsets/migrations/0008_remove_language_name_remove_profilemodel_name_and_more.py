# Generated by Django 4.0.3 on 2022-03-15 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formsets', '0007_language_levelofskill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profilemodel',
            name='name',
        ),
        migrations.AddField(
            model_name='language',
            name='skillname',
            field=models.CharField(max_length=100, null=True, verbose_name='مهارت'),
        ),
    ]
