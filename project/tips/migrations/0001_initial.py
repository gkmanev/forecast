# Generated by Django 3.2.6 on 2023-01-13 19:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OverTwoAndHalf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homeTeam', models.CharField(max_length=400)),
                ('awayTeam', models.CharField(max_length=400)),
                ('startTime', models.DateTimeField(default=datetime.datetime(2023, 1, 13, 21, 57, 54, 549342))),
                ('home_over_percentage', models.IntegerField()),
                ('away_over_percentage', models.IntegerField()),
                ('championship', models.CharField(max_length=400)),
                ('bet_url', models.CharField(max_length=600)),
            ],
        ),
    ]
