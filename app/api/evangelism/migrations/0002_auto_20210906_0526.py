# Generated by Django 3.2.4 on 2021-09-06 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evangelism', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evangelism',
            name='member',
        ),
        migrations.RemoveField(
            model_name='evangelism',
            name='minister',
        ),
        migrations.RemoveField(
            model_name='evangelism',
            name='ministry',
        ),
    ]
