# Generated by Django 3.2.13 on 2022-06-20 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('departments', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='nome',
            new_name='name',
        ),
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='companies.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='departments',
            field=models.ManyToManyField(to='departments.Department'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
    ]