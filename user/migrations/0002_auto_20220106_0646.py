# Generated by Django 4.0.1 on 2022-01-06 06:46

from django.db import migrations
import csv
from django.conf import settings
from pathlib import Path


def create_dummy_users(apps, schema_editor):
    LipiUser = apps.get_model('user', 'LipiUser')

    with open(settings.BASE_DIR / Path('user/migrations/dummy_data.csv')) as file:
        csv_reader = csv.DictReader(file)
        for data in csv_reader:
            LipiUser.objects.create(**data)


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_dummy_users)
    ]
