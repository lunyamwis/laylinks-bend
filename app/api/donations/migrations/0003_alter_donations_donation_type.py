# Generated by Django 3.2.4 on 2021-09-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_alter_donations_donation_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='donation_type',
            field=models.CharField(choices=[('S', 'Special Needs'), ('MS', 'Support Minister'), ('MIS', 'Support a Ministry'), ('L', 'Laylinks')], default='S', max_length=50),
        ),
    ]
