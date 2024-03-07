# Generated by Django 5.0.2 on 2024-03-07 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0008_alter_vaccine_date_of_approval_alter_vaccine_dosage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='days',
            field=models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], default='Mon', max_length=3),
        ),
        migrations.AddField(
            model_name='doctor',
            name='fees',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='doctor_images/'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='time',
            field=models.CharField(default='10:00-18:00', max_length=100),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='nutrition_images/'),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='breast_milk_composition',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='formula_milk_composition',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='introduction_of_solids',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='recommended_diet',
            field=models.TextField(blank=True, null=True),
        ),
    ]
