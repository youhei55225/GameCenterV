# Generated by Django 3.2.12 on 2022-06-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0004_auto_20220612_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memos',
            name='my_char',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='memos',
            name='opp_char',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]