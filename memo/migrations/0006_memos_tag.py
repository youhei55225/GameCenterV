# Generated by Django 3.2.12 on 2022-06-12 17:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0005_auto_20220612_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='memos',
            name='tag',
            field=models.CharField(default=datetime.datetime(2022, 6, 12, 17, 34, 20, 471850, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
