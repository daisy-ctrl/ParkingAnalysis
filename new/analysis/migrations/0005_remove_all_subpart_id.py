# Generated by Django 3.1 on 2020-08-14 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0004_auto_20200814_0736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='all',
            name='subpart_id',
        ),
    ]