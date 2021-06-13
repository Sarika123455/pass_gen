# Generated by Django 3.1.7 on 2021-06-05 10:15

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0008_auto_20210605_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_loan_choice',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('RD Member', 'RD Member'), ('Loan Member', 'Loan Member')], max_length=50),
        ),
    ]
