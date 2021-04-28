# Generated by Django 3.2 on 2021-04-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('als', '0005_alter_al_activated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='al',
            old_name='activated',
            new_name='training_activated',
        ),
        migrations.AddField(
            model_name='al',
            name='is_quering',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='al',
            name='testing_activated',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]