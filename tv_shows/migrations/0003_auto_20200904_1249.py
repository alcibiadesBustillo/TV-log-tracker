# Generated by Django 3.1.1 on 2020-09-04 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows', '0002_auto_20200904_1248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spent',
            old_name='finaltime_time',
            new_name='final_time',
        ),
    ]
