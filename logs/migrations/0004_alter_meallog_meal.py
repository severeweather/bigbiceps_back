# Generated by Django 5.0.7 on 2025-04-14 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_remove_meallog_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meallog',
            name='meal',
            field=models.JSONField(default=dict),
        ),
    ]
