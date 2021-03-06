# Generated by Django 3.2.13 on 2022-06-20 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_user'),
        ('overtime_registration', '0002_overtimeregistration_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overtimeregistration',
            name='employee',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='employees.employee'),
            preserve_default=False,
        ),
    ]
