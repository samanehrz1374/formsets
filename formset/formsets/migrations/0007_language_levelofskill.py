# Generated by Django 4.0.3 on 2022-03-15 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formsets', '0006_remove_book_user_profilemodel_user_alter_book_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='levelofskill',
            field=models.IntegerField(choices=[(1, 'مقدماتی'), (2, 'متوسط'), (3, 'پیشرفته')], null=True, verbose_name='سطح مهارت'),
        ),
    ]
