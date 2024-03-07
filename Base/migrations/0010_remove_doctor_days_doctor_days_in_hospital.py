# Generated by Django 5.0.2 on 2024-03-07 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0009_doctor_days_doctor_fees_doctor_image_doctor_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='days',
        ),
        migrations.AddField(
            model_name='doctor',
            name='days_in_hospital',
            field=models.CharField(blank=True, choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], max_length=50, null=True),
        ),
    ]
