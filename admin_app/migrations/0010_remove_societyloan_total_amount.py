# Generated by Django 3.1.7 on 2021-06-06 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0009_auto_20210605_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='societyloan',
            name='total_amount',
        ),
    ]
