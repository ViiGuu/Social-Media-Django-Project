# Generated by Django 5.1.3 on 2024-11-25 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0003_alter_profile_created_at_alter_profile_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='updated_at',
            field=models.DateField(),
        ),
    ]
