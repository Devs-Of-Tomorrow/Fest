# Generated by Django 3.2.6 on 2021-09-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_festevent_event_on_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='festevent',
            old_name='eventprice',
            new_name='fees',
        ),
        migrations.AlterField(
            model_name='festevent',
            name='event_on_day',
            field=models.CharField(blank=True, choices=[('1', 'Day 1️⃣'), ('2', 'Day 2️⃣'), ('3', 'Day 3️⃣'), ('4', 'Day 4️⃣'), ('5', 'Day 5️⃣'), ('6', 'Day 6')], default='Choose Day', max_length=20),
        ),
        migrations.AlterField(
            model_name='festevent',
            name='participation_type',
            field=models.CharField(blank=True, choices=[('individual', ' 👱🏻 Individual'), ('team', '👨\u200d👩\u200d👦 Team ')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='festevent',
            name='venue',
            field=models.CharField(choices=[('0', 'Patkar College 😒'), ('1', "Bhavan's College 😌"), ('2', 'Virtual')], default='2', max_length=30, null=True),
        ),
    ]