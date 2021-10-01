# Generated by Django 3.2.4 on 2021-08-30 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('minister', '0001_initial'),
        ('member', '0001_initial'),
        ('ministry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evangelism',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('id', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('field', models.CharField(choices=[('PR', 'Preacher'), ('P', 'Prophecy'), ('M', 'Medical'), ('PE', 'Personal Evangelism'), ('CH', 'Child Evangelism'), ('SO', 'Song Evangelism'), ('C', 'City Evangelism'), ('D', 'Disability Evangelism'), ('S', 'Special Classes Evangelism'), ('BS', 'Bible Study Evangelism'), ('PU', 'Publishing Evangelism'), ('L', 'Lay Evangelism')], default='PE', max_length=50)),
                ('event', models.CharField(choices=[('HE', 'Health Expo'), ('P', 'Personal'), ('PU', 'Public Effort'), ('M', 'Hall Meetings'), ('L', 'Live Streaming'), ('R', 'Recorded Message'), ('MD', 'Printed Material Distribution'), ('S', 'Sermon')], default='P', max_length=50)),
                ('event_name', models.TextField(max_length=1024)),
                ('event_date', models.DateTimeField()),
                ('event_location', models.CharField(max_length=255)),
                ('event_purpose', models.TextField()),
                ('event_duration', models.CharField(max_length=1024)),
                ('sermon_theme', models.TextField()),
                ('sermon_length', models.IntegerField()),
                ('number_attendees', models.IntegerField()),
                ('budget', models.FloatField()),
                ('number_converts', models.IntegerField()),
                ('number_followups', models.IntegerField()),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.member')),
                ('minister', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='minister.minister')),
                ('ministry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ministry.ministry')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
