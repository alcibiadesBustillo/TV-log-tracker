# Generated by Django 3.1.1 on 2020-09-04 12:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spent',
            name='finaltime_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spent',
            name='initial_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
