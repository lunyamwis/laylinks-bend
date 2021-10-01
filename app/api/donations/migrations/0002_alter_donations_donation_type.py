# Generated by Django 3.2.4 on 2021-09-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='donation_type',
            field=models.CharField(choices=[('S', 'Special Needs'), ('MS', 'Support Minister'), ('MIS', 'Support a Ministry')], default='S', max_length=50),
        ),
    ]