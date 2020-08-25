# Generated by Django 3.1 on 2020-08-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0015_delete_busiesthour'),
    ]

    operations = [
        migrations.CreateModel(
            name='average_daily_transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('Weekday_Name', models.CharField(max_length=10)),
                ('Sub_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='busiest_hour',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Hour', models.IntegerField()),
                ('Sub_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='busiest_subcounty',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Sub_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='busiest_subcounty_by_weekday',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Weekday_Name', models.CharField(max_length=10)),
                ('Sub_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='daily_traffic_count',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Weekday_Name', models.CharField(max_length=10)),
                ('Sub_name', models.CharField(max_length=20)),
            ],
        ),
    ]
