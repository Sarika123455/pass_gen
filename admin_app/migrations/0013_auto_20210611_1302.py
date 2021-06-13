# Generated by Django 3.2.4 on 2021-06-11 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0012_member_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='societyloan',
            name='total_amount',
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('August', 'August'), ('September', 'September'), ('November', 'November'), ('December', 'December')], max_length=100)),
                ('monthly_pay', models.IntegerField()),
                ('total_paid', models.IntegerField()),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid'), ('Complete Loan', 'Complete Loan')], max_length=100)),
                ('remaining_balance', models.IntegerField()),
                ('member_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.member')),
                ('total_amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.societyloan')),
            ],
        ),
    ]
