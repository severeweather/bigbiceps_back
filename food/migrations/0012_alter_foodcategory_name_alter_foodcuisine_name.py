# Generated by Django 5.0.7 on 2025-06-15 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_alter_nutrient_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcategory',
            name='name',
            field=models.CharField(unique=True),
        ),
        migrations.AlterField(
            model_name='foodcuisine',
            name='name',
            field=models.CharField(unique=True),
        ),
    ]
