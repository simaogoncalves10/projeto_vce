# Generated by Django 3.2 on 2021-04-19 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endoscopies', '0004_alter_endoscopy_id_exam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endoscopy',
            name='id_exam',
        ),
    ]
