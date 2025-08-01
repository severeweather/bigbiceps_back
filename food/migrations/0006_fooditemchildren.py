# Generated by Django 5.0.7 on 2025-05-15 20:09

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_delete_fooditemchildren'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItemChildren',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child', to='food.fooditem')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='food.fooditem')),
            ],
        ),
    ]
