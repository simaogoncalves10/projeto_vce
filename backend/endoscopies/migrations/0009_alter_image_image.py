# Generated by Django 3.2 on 2021-04-24 16:36

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('endoscopies', '0008_remove_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=0, size=[128, 128], upload_to='endoscopies/%Y/%m/%d'),
        ),
    ]
