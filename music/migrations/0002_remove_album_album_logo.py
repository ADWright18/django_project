# Generated by Django 2.0 on 2017-12-27 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_logo',
        ),
    ]
