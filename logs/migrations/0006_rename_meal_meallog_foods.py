# Generated by Django 5.0.7 on 2025-04-19 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0005_alter_progresslog_meal_logs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meallog',
            old_name='meal',
            new_name='foods',
        ),
    ]
