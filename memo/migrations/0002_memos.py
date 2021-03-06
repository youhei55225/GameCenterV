# Generated by Django 3.2.12 on 2022-06-06 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('my_char', models.CharField(max_length=255)),
                ('opp_char', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now=True)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('good', models.PositiveIntegerField()),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
    ]
