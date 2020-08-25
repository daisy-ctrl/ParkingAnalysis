# Generated by Django 3.1 on 2020-08-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0008_remove_all_raw_recorded_date_formatted'),
    ]

    operations = [
        migrations.AddField(
            model_name='all',
            name='Hour',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='all',
            name='Sub_name',
            field=models.CharField(default=10, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='all',
            name='Weekday_Name',
            field=models.CharField(default=10, max_length=10),
            preserve_default=False,
        ),
    ]
