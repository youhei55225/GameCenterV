# Generated by Django 3.2.12 on 2022-06-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0003_auto_20220606_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memos',
            name='my_char',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='memos',
            name='opp_char',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
