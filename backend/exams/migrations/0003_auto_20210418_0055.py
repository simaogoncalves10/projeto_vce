# Generated by Django 3.2 on 2021-04-17 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacients', '0007_alter_pacient_total_exams'),
        ('exams', '0002_auto_20210405_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='id_pacient',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pacients.pacient'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_notes',
            field=models.TextField(default='Undefined', max_length=1000),
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_result',
            field=models.TextField(default='Undefined', max_length=1000),
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_type',
            field=models.CharField(default='Undefined', max_length=100),
        ),
    ]