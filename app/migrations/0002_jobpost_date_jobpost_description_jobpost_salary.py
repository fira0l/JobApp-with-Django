# Generated by Django 5.0.2 on 2024-02-09 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 2, 9, 19, 45, 34, 611210, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='salary',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]