# Generated by Django 3.2.4 on 2021-09-01 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_blog_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='comments',
        ),
        migrations.AddField(
            model_name='comments',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blog'),
        ),
    ]
