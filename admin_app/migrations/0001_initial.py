# Generated by Django 3.1.7 on 2021-06-05 07:39

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True)),
                ('mobile_no', models.IntegerField()),
                ('email_id', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('aadhar_card_number', models.IntegerField()),
                ('pan_card_number', models.CharField(max_length=100)),
                ('aadhar_card_upload', models.ImageField(upload_to='images')),
                ('pan_card_upload', models.ImageField(upload_to='images')),
                ('member_loan_choice', multiselectfield.db.fields.MultiSelectField(choices=[('RD Member', 'RD Member'), ('Loan Member', 'Loan Member')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Societyloan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True)),
                ('start_month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('August', 'August'), ('September', 'September'), ('November', 'November'), ('December', 'December')], max_length=100)),
                ('end_month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('August', 'August'), ('September', 'September'), ('November', 'November'), ('December', 'December')], max_length=100)),
                ('year', models.IntegerField()),
                ('rate_of_interest', models.FloatField()),
                ('loan_amount', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('full_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.member')),
            ],
        ),
    ]
