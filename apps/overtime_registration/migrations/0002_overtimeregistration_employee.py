# Generated by Django 3.2.13 on 2022-06-20 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20220620_1544'),
        ('overtime_registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='overtimeregistration',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee'),
        ),
    ]
