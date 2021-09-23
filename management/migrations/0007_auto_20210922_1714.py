# Generated by Django 3.2.6 on 2021-09-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20210922_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='signinuser',
            name='profile_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='uploads/events/profile_images/'),
        ),
        migrations.AlterField(
            model_name='festevent',
            name='coordinators',
            field=models.CharField(blank=True, choices=[('Amir', 'Amir'), ('Roshith', 'Roshith')], default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='festevent',
            name='event_type',
            field=models.CharField(blank=True, choices=[('Technical', 'Technical'), ('Non-technical', 'Non-Technical'), ('Cultural', 'Cultural'), ('Management', 'Management')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='festevent',
            name='participation_type',
            field=models.CharField(blank=True, choices=[('👱🏻Individual', ' 👱🏻 Individual'), ('👨\u200d👩\u200d👦Team', '👨\u200d👩\u200d👦Team ')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='festevent',
            name='venue',
            field=models.CharField(choices=[('Patkar College 😒', 'Patkar College 😒'), ("Bhavan's College 😌", "Bhavan's College 😌"), ('Virtual', 'Virtual')], default='2', max_length=30, null=True),
        ),
    ]
