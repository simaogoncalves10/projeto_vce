# Generated by Django 3.1.7 on 2021-04-05 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210405_0343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='medic',
        ),
    ]