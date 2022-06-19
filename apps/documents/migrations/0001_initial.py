# Generated by Django 3.2.13 on 2022-06-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_id', models.IntegerField(help_text='register document number', null=True)),
                ('description', models.CharField(help_text='text description document', max_length=150)),
            ],
        ),
    ]