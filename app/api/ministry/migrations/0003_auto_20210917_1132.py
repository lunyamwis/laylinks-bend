# Generated by Django 3.2.4 on 2021-09-17 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ministry', '0002_auto_20210906_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ministry',
            name='home_church_phone_numbers',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ministry',
            name='phone_numbers',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
