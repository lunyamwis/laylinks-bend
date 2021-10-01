# Generated by Django 3.2.4 on 2021-08-30 14:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('id', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('phone_numbers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200, null=True), size=None)),
                ('category', models.CharField(choices=[('I', 'Self Supporting'), ('C', 'Supported Church')], default='I', max_length=50)),
                ('conference_name', models.CharField(max_length=255)),
                ('field_name', models.CharField(max_length=255)),
                ('home_church_name', models.TextField()),
                ('home_church_email', models.EmailField(max_length=254)),
                ('home_church_phone_numbers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200, null=True), size=None)),
                ('home_church_location', models.CharField(max_length=50)),
                ('church_elder_first_name', models.CharField(max_length=50)),
                ('church_elder_last_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
