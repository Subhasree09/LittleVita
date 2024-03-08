# Generated by Django 5.0.2 on 2024-03-03 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0005_alter_parent_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parent',
            old_name='parent_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='parent',
            old_name='parent_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='parent',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]