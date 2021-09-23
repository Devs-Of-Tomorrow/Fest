# Generated by Django 3.2.6 on 2021-09-22 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_delete_countries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('1', 'Title Sponsor'), ('2', 'Online Media Sponsors'), ('3', 'Normal Sponsor'), ('4', 'Event Sponsor')], max_length=20)),
                ('name', models.CharField(blank=True, default='', max_length=30)),
                ('name_shown', models.CharField(blank=True, default='', max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='uploads/events/sponsors/')),
                ('url', models.URLField(blank=True, default='')),
            ],
            options={
                'verbose_name_plural': 'Sponsors',
            },
        ),
    ]