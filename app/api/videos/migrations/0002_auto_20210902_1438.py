# Generated by Django 3.2.4 on 2021-09-02 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('id', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('id', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='video',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='video',
            name='tags',
        ),
        migrations.AddField(
            model_name='video',
            name='categories',
            field=models.ManyToManyField(to='videos.Categories'),
        ),
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(to='videos.Tags'),
        ),
    ]
