# Generated by Django 5.0.2 on 2024-03-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0014_alter_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(default='doctor_images/default_image.jpg', upload_to='doctor_images/'),
        ),
    ]
