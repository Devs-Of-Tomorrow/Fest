# Generated by Django 3.2.6 on 2021-10-08 12:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_alter_signinuser_date_joined'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signinuser',
            old_name='universitiy',
            new_name='university',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female', 'Female'), ('male', 'Male'), ('Other', 'Other')], default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='signinuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 8, 17, 30, 42, 532965)),
        ),
    ]
