# Generated by Django 5.0.7 on 2025-03-01 14:05

import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_activity_level_customuser_body_fat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeightProgressLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_logged', models.DateField(auto_now_add=True)),
                ('weight', models.IntegerField()),
                ('body_fat', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('activity_level', models.CharField(choices=[('sed', 'Sedentary'), ('lig', 'Lightly active'), ('mod', 'Moderately active'), ('ver', 'Very active'), ('ext', 'Extremely active')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
