# Generated by Django 4.1.4 on 2023-04-07 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perpage',
            name='user',
        ),
    ]
