# Generated by Django 3.1 on 2020-08-15 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0005_remove_all_subpart_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='all',
            old_name='part_id',
            new_name='subcounty_id',
        ),
        migrations.RemoveField(
            model_name='all',
            name='record_date',
        ),
        migrations.RemoveField(
            model_name='all',
            name='transaction_mode_id',
        ),
    ]