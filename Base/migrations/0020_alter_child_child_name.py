# Generated by Django 5.0.2 on 2024-03-08 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0019_child_child_sex_alter_child_vaccine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='child_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]