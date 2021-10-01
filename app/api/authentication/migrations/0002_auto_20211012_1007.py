# Generated by Django 3.2.4 on 2021-10-12 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minister', '0003_alter_minister_home_church_phone_numbers'),
        ('member', '0002_alter_member_home_church_phone_numbers'),
        ('ministry', '0003_auto_20210917_1132'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authentication_user_related', related_query_name='authentication_users', to='member.member'),
        ),
        migrations.AddField(
            model_name='user',
            name='minister',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authentication_user_related', related_query_name='authentication_users', to='minister.minister'),
        ),
        migrations.AddField(
            model_name='user',
            name='ministry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authentication_user_related', related_query_name='authentication_users', to='ministry.ministry'),
        ),
    ]
