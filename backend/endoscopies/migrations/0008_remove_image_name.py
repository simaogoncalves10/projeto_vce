# Generated by Django 3.2 on 2021-04-20 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endoscopies', '0007_alter_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
    ]