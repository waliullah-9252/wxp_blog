# Generated by Django 4.2.7 on 2024-03-04 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
